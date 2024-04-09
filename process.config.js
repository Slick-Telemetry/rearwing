module.exports = {
  apps: [
    {
      name: "slick_telemetry_backend",
      script: "uvicorn",
      interpreter: "./.venv/bin/python",
      args: "app.main:app --host 0.0.0.0 --port 8081",
      autorestart: true,
      // max_memory_restart: "300M",
      restart_delay: 30, // seconds
      // watch: true,
      // env: {
      //   NODE_ENV: "development",
      // },
      // env_production: {
      //   NODE_ENV: "production",
      // },
    },
  ],
};
