import React from "react";
import CountUp from "react-countup";

export default function Dashboard() {
  const jobs = [
    "TCS opened 20 Fresher Roles",
    "Infosys hiring System Engineers",
    "Accenture hiring Associate Developers",
  ];

  const applications = [
    { company: "TCS", status: "Applied" },
    { company: "Infosys", status: "Interview" },
    { company: "Accenture", status: "Shortlisted" },
    { company: "Capgemini", status: "Rejected" },
  ];

  const recommendations = [
    {
      role: "Java Developer",
      company: "TCS",
      match: "95%",
    },
    {
      role: "Spring Boot Engineer",
      company: "Infosys",
      match: "91%",
    },
    {
      role: "Software Engineer",
      company: "Accenture",
      match: "88%",
    },
  ];

  return (
    <div className="min-h-screen bg-slate-950 text-white p-6">
      
      {/* Header */}
      <div className="flex justify-between items-center mb-8">
        <h1 className="text-4xl font-bold">
          CareerBridge AI 🚀
        </h1>

        <button className="bg-cyan-500 px-5 py-2 rounded-lg font-semibold">
          Upgrade Pro
        </button>
      </div>

      {/* Welcome */}
      <div className="bg-slate-900 rounded-2xl p-6 mb-6">
        <h2 className="text-2xl font-bold">
          Welcome Back 👋
        </h2>

        <p className="text-slate-400 mt-2">
          Your career dashboard is looking great today.
        </p>

        <div className="mt-4 flex gap-3 flex-wrap">
          <span className="bg-yellow-500 text-black px-3 py-1 rounded-full">
            ⭐ Level 7
          </span>

          <span className="bg-green-500 text-black px-3 py-1 rounded-full">
            🏆 Interview Warrior
          </span>

          <span className="bg-purple-500 px-3 py-1 rounded-full">
            XP: 1240
          </span>
        </div>
      </div>

      {/* Stats */}
      <div className="grid md:grid-cols-4 gap-4 mb-8">
        
        <div className="bg-slate-900 p-5 rounded-2xl">
          <p className="text-slate-400">New Jobs</p>
          <h2 className="text-4xl font-bold">
            <CountUp end={128} duration={2} />
          </h2>
        </div>

        <div className="bg-slate-900 p-5 rounded-2xl">
          <p className="text-slate-400">Applications</p>
          <h2 className="text-4xl font-bold">
            <CountUp end={24} duration={2} />
          </h2>
        </div>

        <div className="bg-slate-900 p-5 rounded-2xl">
          <p className="text-slate-400">Interview Calls</p>
          <h2 className="text-4xl font-bold">
            <CountUp end={4} duration={2} />
          </h2>
        </div>

        <div className="bg-slate-900 p-5 rounded-2xl">
          <p className="text-slate-400">Profile Strength</p>
          <h2 className="text-4xl font-bold">
            <CountUp end={82} duration={2} />%
          </h2>
        </div>

      </div>

      <div className="grid lg:grid-cols-2 gap-6">

        {/* Live Feed */}
        <div className="bg-slate-900 rounded-2xl p-6">
          <h2 className="text-2xl font-bold mb-4">
            🚨 Live Hiring Feed
          </h2>

          {jobs.map((job, index) => (
            <div
              key={index}
              className="bg-slate-800 p-3 rounded-lg mb-3"
            >
              {job}
            </div>
          ))}
        </div>

        {/* AI Recommendations */}
        <div className="bg-slate-900 rounded-2xl p-6">
          <h2 className="text-2xl font-bold mb-4">
            🤖 AI Recommendations
          </h2>

          {recommendations.map((job, index) => (
            <div
              key={index}
              className="bg-slate-800 p-4 rounded-lg mb-3"
            >
              <h3 className="font-bold text-lg">
                {job.role}
              </h3>

              <p>{job.company}</p>

              <span className="text-green-400">
                Match Score: {job.match}
              </span>
            </div>
          ))}
        </div>

      </div>

      {/* Applications */}
      <div className="bg-slate-900 rounded-2xl p-6 mt-6">
        <h2 className="text-2xl font-bold mb-4">
          📊 Application Tracker
        </h2>

        <table className="w-full">
          <thead>
            <tr className="border-b border-slate-700">
              <th className="text-left py-3">Company</th>
              <th className="text-left py-3">Status</th>
            </tr>
          </thead>

          <tbody>
            {applications.map((app, index) => (
              <tr
                key={index}
                className="border-b border-slate-800"
              >
                <td className="py-3">{app.company}</td>
                <td className="py-3">{app.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

    </div>
  );
}