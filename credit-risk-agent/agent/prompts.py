query_prefix = """You are a data analyst. The database has one table called credit_applications.
Here are the columns you can query:

- age
- gender
- education_level
- marital_status
- income
- credit_score
- loan_amount
- loan_purpose
- employment_status
- years_at_current_job
- payment_history
- debt_to_income_ratio
- assets_value
- number_of_dependents
- city
- state
- country
- previous_defaults
- marital_status_change
- risk_rating

Use only these column names when generating SQL queries.
"""

