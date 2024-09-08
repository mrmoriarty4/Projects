select* from layoffs_staging;

select *,
 row_number() over(partition by company, location, industry, total_laid_off, percentage_laid_off, `date`) as row_num
 from layoffs_staging;
 
 with duplicate_cte as
 (select *,
 row_number() over(partition by company, location, industry, total_laid_off, percentage_laid_off, `date`, stage, country, funds_raised_millions) as row_num
 from layoffs_staging)
 
 select * 
 from duplicate_cte
 where row_num > 1;
 
CREATE TABLE `layoffs_staging2` (
  `company` text,
  `location` text,
  `industry` text,
  `total_laid_off` int DEFAULT NULL,
  `percentage_laid_off` text,
  `date` text,
  `stage` text,
  `country` text,
  `funds_raised_millions` int DEFAULT NULL,
  `row_num` int 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

insert into layoffs_staging2
(select *,
 row_number() over(partition by company, location, industry, total_laid_off, percentage_laid_off, `date`, stage, country, funds_raised_millions) as row_num
 from layoffs_staging);
 
 select * from layoffs_staging2;

SET SQL_SAFE_UPDATES = 0;
delete
from layoffs_staging2
where row_num > 1;

select*
from layoffs_staging2
where row_num > 1;

select company, trim(company)
from layoffs_staging2;

update layoffs_staging2
set company = trim(company);

select distinct industry
from layoffs_staging2
order by 1;

update layoffs_staging2
set industry = 'Crypto'
where industry like 'Crypto%';

select *
from layoffs_staging2
where industry like'Crypto%';

select distinct location
from layoffs_staging2
order by 1;

select distinct country
from layoffs_staging2
order by 1;

update layoffs_staging2
set country = TRIM( trailing '.' from country)
where country like 'United States%';

select distinct country
from layoffs_staging2
order by 1;

select `date`, str_to_date(`date`, '%m/%d/%Y')
from layoffs_staging2;

update layoffs_staging2
set `date` = str_to_date(`date`, '%m/%d/%Y');

select `date`
from layoffs_staging2;

alter table layoffs_staging2
modify column `date` date;

select * from layoffs_staging2;

select * from layoffs_staging2
where total_laid_off is null;

select *
from layoffs_staging2 as t1
join layoffs_staging2 as t2
	on t1.company = t2.company
where (t1.industry is null or t1.industry = '')
and t2.industry is not null;

update layoffs_staging2
set industry = null 
where industry = '';

update layoffs_staging2 as t1
join layoffs_staging2 as t2
	on t1.company = t2.company
set t1.industry = t2.industry
where t1.industry is null 
and t2.industry is not null;

select * from layoffs_staging2
where company = 'Airbnb';

select * from layoffs_staging2
where industry is null or industry = '';

select * from layoffs_staging2
where company like 'Bally%';

select Max(total_laid_off)
from layoffs_staging2;

select Max(percentage_laid_off)
from layoffs_staging2;

select *
from layoffs_staging2
where percentage_laid_off = 1;
-- order by funds_raised_millions desc; -- 

select company, total_laid_off
from layoffs_staging2
order by 2 desc;
-- Limit 5; --

select company, sum(total_laid_off)
from layoffs_staging2
group by company
order by 2 desc;
-- Limit 10; --

select location, sum(total_laid_off)
from layoffs_staging2
group by location
order by 2 desc;
-- Limit 10; --

select year(`date`), sum(total_laid_off)
from layoffs_staging2
group by year(`date`)
order by 2 desc;

WITH Cte_Company_Year AS 
(
  SELECT company, YEAR(`date`) AS years, SUM(total_laid_off) AS total_laid_off
  FROM layoffs_staging2
  GROUP BY company, YEAR(`date`)
),
Cte_Company_Year_Rank AS (
  SELECT company, years, total_laid_off, DENSE_RANK() OVER (PARTITION BY years ORDER BY total_laid_off DESC) AS ranking
  FROM Cte_Company_Year
)
SELECT company, years, total_laid_off, ranking
from Cte_Company_Year_Rank
where years is not null -- and ranking <=3 -- 
order by years asc, total_laid_off desc;

SELECT SUBSTRING(date,1,7) as dates, SUM(total_laid_off) AS total_laid_off
FROM layoffs_staging2
GROUP BY dates
ORDER BY dates ASC;

WITH DATE_CTE AS 
(
SELECT SUBSTRING(date,1,7) as dates, SUM(total_laid_off) AS total_laid_off
FROM layoffs_staging2
GROUP BY dates
ORDER BY dates ASC
)
SELECT dates, SUM(total_laid_off) OVER (ORDER BY dates ASC) as rolling_total_layoffs
FROM DATE_CTE
ORDER BY dates ASC;