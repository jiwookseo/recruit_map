const axios = require("axios");
const apiKey = process.env["SARAMIN_KEY"];
res = axios
  .get(
    `http://oapi.saramin.co.kr/job-search/?access-key=${apiKey}&sr=directhire&loc_cd=101000, 102000&ind_cd=3&bbs_gb=1&count=110`,
    { Accept: "application/json" }
  )
  .then(res => {
    console.log(res.data.jobs.total);
    const jobs = res.data.jobs.job;
    jobs.forEach(job => {
      console.log(job.company.detail.name);
      console.log(job.position.title);
      console.log(job.salary.name);
    });
  });
// 기업 주소, 평균 연봉 등 데이터 수집 필요
