# Vercel Deployment Guide

This guide will help you deploy the Vibe Music Django application to Vercel.

## Prerequisites

1. Vercel account
2. GitHub repository connected to Vercel
3. All environment variables configured

## Files Created for Vercel Deployment

### 1. `vercel.json`
- Configures build settings and routing
- Sets up static file serving
- Defines Python runtime

### 2. `music_club/asgi_vercel.py`
- ASGI configuration for Vercel
- Handles Django application startup

### 3. `start.sh`
- Startup script for collecting static files
- Runs database migrations
- Starts the server

### 4. Updated `requirements.txt`
- Added `whitenoise>=6.0.0` for static file serving
- Added `gunicorn>=21.0.0` for production server

### 5. Updated `music_club/settings.py`
- Added whitenoise middleware and app
- Configured static file settings
- Added Vercel-specific security settings
- Updated DEBUG and ALLOWED_HOSTS for production

## Environment Variables

Set these in your Vercel dashboard under Environment Variables:

```
DEBUG=False
DJANGO_SETTINGS_MODULE=music_club.settings
SECRET_KEY=your_production_secret_key_here
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
RAZORPAY_KEY_ID=your_razorpay_key_id
RAZORPAY_KEY_SECRET=your_razorpay_key_secret
```

## Deployment Steps

1. **Push all changes to GitHub**
   ```bash
   git add .
   git commit -m "Add Vercel deployment configuration"
   git push origin main
   ```

2. **Connect to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Select the Django framework preset

3. **Configure Environment Variables**
   - Go to your project settings in Vercel
   - Add all environment variables listed above
   - Make sure to set `DEBUG=False` for production

4. **Deploy**
   - Click "Deploy"
   - Vercel will automatically build and deploy your application

## Common Issues and Solutions

### 1. Static Files Not Loading
- Ensure `STATIC_ROOT` is set in settings.py
- Make sure `whitenoise` is properly configured
- Check that static files are collected during build

### 2. Database Connection Issues
- Vercel doesn't include a database by default
- Consider using Vercel Postgres or an external database
- Update DATABASE_URL environment variable

### 3. Media Files Not Serving
- Media files need external storage (AWS S3, Cloudinary, etc.)
- Vercel's filesystem is read-only after deployment

### 4. CSRF Issues
- Ensure CSRF_TRUSTED_ORIGINS includes your Vercel domain
- Check that CSRF cookies are properly configured

## Post-Deployment Checklist

- [ ] All static files are loading correctly
- [ ] Database migrations have run
- [ ] Environment variables are set correctly
- [ ] HTTPS is working (automatic on Vercel)
- [ ] Contact form emails are sending
- [ ] Payment integration is working
- [ ] All pages are accessible and functional

## Monitoring and Debugging

1. **Vercel Logs**: Check the Functions tab in your Vercel dashboard
2. **Django Debug Toolbar**: Disable in production (already handled)
3. **Error Tracking**: Consider integrating Sentry for error monitoring

## Performance Optimization

1. **Static File Compression**: Enabled by whitenoise
2. **Database Optimization**: Use connection pooling
3. **Caching**: Consider Redis for caching
4. **CDN**: Vercel provides automatic CDN

## Security Considerations

1. **SECRET_KEY**: Use a strong, unique secret key
2. **DEBUG**: Always set to False in production
3. **HTTPS**: Automatically enabled by Vercel
4. **Environment Variables**: Never commit secrets to git

## Custom Domain (Optional)

1. Go to your project settings in Vercel
2. Click "Domains"
3. Add your custom domain
4. Update DNS records as instructed by Vercel

## Support

If you encounter issues:
1. Check Vercel deployment logs
2. Review Django error messages
3. Ensure all environment variables are set
4. Verify static files are properly collected
