---
description: How to access and run the Gear Exchange page
---

# Gear Exchange Page Workflow

This workflow explains how to access and run the Gear Exchange (Used Gear) marketplace page.

## Accessing the Gear Exchange Page

The Gear Exchange page can be accessed through the following URLs:

1. **Direct URL**: `http://127.0.0.1:8000/user/used-gear/`
2. **Redirect URL**: `http://127.0.0.1:8000/used/` (redirects to `/user/used-gear/`)

## Running the Development Server

1. Open a terminal in the project root directory
2. Run the Django development server:
   ```
   python manage.py runserver
   ```
3. Open your browser and navigate to one of the URLs above

## Page Features

The Gear Exchange page includes:

- **Search functionality**: Search bar for finding used gear
- **Category filters**: Filter by gear categories (Guitars, Effects & Pedals, Amplifiers, Bass, Keyboards & Synthesizers, Microphones & Wireless, Live Sound & Lighting, Studio & Recording Gear, Drums & Percussion, Band & Orchestra, DJ / Electronic)
- **Hero banner**: Promotional section for selling used gear
- **Feature highlights**: No Commission, Secure Transactions, Easy Shipping, Trusted Community
- **Featured listings**: Grid of sample product listings with condition badges, prices, and seller ratings
- **CTA section**: Call-to-action for creating listings

## Files Modified

- `music_club/urls.py`: Added redirect for `/used/`
- `User/urls.py`: Added URL patterns for `used/` and `used-gear/`
- `User/views.py`: Added `used_gear_page` view function
- `templates/user/used_gear.html`: Gear Exchange marketplace page template

## Future Enhancements

To make the page fully functional, consider adding:

1. Backend models for gear listings
2. Database integration for storing listings
3. User authentication for creating listings
4. Search functionality with Algolia or similar
5. Category filtering logic
6. Listing detail pages
7. Seller profile pages
8. Payment integration for purchases
