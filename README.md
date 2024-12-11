# CarBlog

### Deployed version: https://https://carblog-fhczg0adajejghh3.italynorth-01.azurewebsites.net/
### Recommended resolution on computer: 1920x1080

### Prerequisites
- Python and Django installed.


### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/danisp24/car_blog.git
   ```

2. Install requirements.txt:
   ```sh
   pip install requirements.txt
   ```

3. Users and groups:
   ## Here are the created users and Groups for testing purposes
 ```sh
   https://github.com/danisp24/car_blog/blob/main/users%20and%20groups
   ```

## Features
### Authentication
- **Register**: Users can register, providing Username, First Name, Last Name, Gender, Email, Password and Confirm Password - error messages are displayed if the values are not in the correct format. - First Name, Last Name and Gender are optional.
- **Login**: Users can log in to their account after it has been created.
- **Logout**: Users can log out of their accounts after they have been logged in.

- Header if user is logged in:
![image](https://github.com/user-attachments/assets/0e02b22a-cd7c-4afb-b9d3-e10cefebba7f)

- Header if user is not logged:
![image](https://github.com/user-attachments/assets/c9f6d9a8-97ed-43e4-b08a-01b695836fef)

- Header if superadmin is logged in:
![image](https://github.com/user-attachments/assets/a7f7eb2f-825b-4928-8e23-fa12e718a0cf)

- Footer:
- ![image](https://github.com/user-attachments/assets/539c973c-2d11-48c8-af7b-80c27dcb1a70)

### Homepage

Normal authenticated user:
![image](https://github.com/user-attachments/assets/fe1b494a-db68-4488-8570-2ca4b90fd212)

User with Post Manager Group:
- Can publish and unpublish posts
![image](https://github.com/user-attachments/assets/80782da0-a5c5-4f2d-9861-24240d367579)

Homepage without user:
![image](https://github.com/user-attachments/assets/4669ba62-04e7-4db4-9b7d-ac3ba15b8a67)
![image](https://github.com/user-attachments/assets/ef3e4079-1030-47ff-8ec0-ce9f40b6edef)

- Learn more about our cars Button leads to Our Cars
- Browse Categories Button leads to Car Categories
- Get Involved Button leads to Registration page



### Authenticated user Create Post:
- Users can create posts about the cars that are in "Our Cars" - with One or Many relations
- Users can create posts without any relations aswell
- The posts have to be Approved by Post moderators - Publish/Unpublish -> is_published = True/False
![image](https://github.com/user-attachments/assets/01b9e62b-33c9-4f67-9cc0-569b1e27fc01)

### Our Cars
- This is accessible by authenticated and unauthenticated users:
- ![image](https://github.com/user-attachments/assets/385eb92c-ac62-43f7-b40d-36ffe5ed0a5d)

### Our Categories
- This is accessible by authenticated and unauthenticated users:
- Unauthenticated users can only see the first page of categories:
![image](https://github.com/user-attachments/assets/972d4a34-5601-4905-98cc-459e0bd00c04)

- Authenticated users can see all the pages:
- ![image](https://github.com/user-attachments/assets/b5dafe71-c833-4ff2-830c-a4e460d850bc)


- Can be Added by Create Category by users with "Car and CarCategory Manager" group and edited and deleted in the admin panel
- ![image](https://github.com/user-attachments/assets/99cd6852-b785-4dbd-b32d-71ec52c4d32e)

  

### Car Bookings
-Only for authenticated users:
- My bookings history:
- Can cancel(Delete) confirmed and cancelled bookings
- Pending bookings can be edited aswell
- Validation that the bookings are in the future
- Signals to change booking status
![image](https://github.com/user-attachments/assets/bb532ef0-66af-4493-86f4-451c645e45a7)

- Manage bookings:
- Only for staff users in group "TestDriveBooking Manager":
- Can approve/cancel bookings
- Also managable in the admin panel
![image](https://github.com/user-attachments/assets/46044107-3f42-4990-add0-a53ff90e2f08)


- Authenticated users can create bookings here:
- They have to wait for the booking staff to Confirm/Cancel their request
- They can only book cars that are available for test drive
- If 2 or more bookings are created at the same time with status "Pending", staff users can approve 1 of them and others are switched to "Cancelled"
![image](https://github.com/user-attachments/assets/a5641bff-b7eb-496e-9ff8-ae8dc3703cd0)

- If car manager tries to book 2 bookings of the same car a custom Http400 error page shows:
![image](https://github.com/user-attachments/assets/ed9c02eb-0a5a-4d05-9249-43fd138136c5)


### Add Car
- Users with group "Car and CarCategory Manager can add cars from here:
![image](https://github.com/user-attachments/assets/e9e433db-8049-4ed7-95cd-e79f82d6025f)
- They can also manage it in the admin panel


### My Account
- This is accessible only to authenticated users:
![image](https://github.com/user-attachments/assets/7190cf0f-1f29-4805-8e3f-953c888f51fc)

- Edit Account so users can Edit their First Name, Last Name and Gender, becuase they are optional in the Registration form:
![image](https://github.com/user-attachments/assets/9ca0fb9e-a023-45e0-90a5-bf6b55fd04e8)

### My Blog
- Button for posts that are created by the user
- They can be edited and deleted from there
![image](https://github.com/user-attachments/assets/966e8374-b62f-43f1-a266-1df171f2f8cb)

### Post Detail Page
- Post detail page shows the comments about the post
- Users can edit and delete their own comments
- The related cars are displayed there and can be clicked to view their Details
![image](https://github.com/user-attachments/assets/146e9349-0fb4-4709-80e8-3add60d97997)

### Comments
- Comments can be moderated by admins with the group "Post Manager" from the admin panel



### 403 Custom Permission Denied page
![image](https://github.com/user-attachments/assets/c98ed037-2cfd-4815-9f87-e708546c1da3)

### 404 Custom Page
![image](https://github.com/user-attachments/assets/167d2000-6222-432f-995a-03953afda6bb)



### Users and Groups for Testing

#### Superuser:
- **Username**: dani
- **Password**: admin
- **Email**: dani@dani.bg

#### Normal User:
- **Username**: user
- **Password**: 12user34
- **Email**: user@user.com

#### Admin (Post Manager):
- **Username**: postmoderator
- **Password**: 12admin34
- **Email**: postmoderator@mail.com

#### Superadmin (not superuser):
- **Username**: superadmin
- **Password**: 12admin34
- **Email**: superadmin@mail.com

#### Admin (Car and CarCategory Manager also TestDriveBookingManager):
- **Username**: carmoderator
- **Password**: 12admin34
- **Email**: carmoderator@mail.com

### Groups and Permissions

- **Superadmin**: All permissions, but `is_superuser = False`.
- **Car and CarCategory Manager**: 
  - CRUD operations on cars.
  - CRUD operations on car categories.
- **Posts Manager**:
  - CRUD operations on posts.
  - CRUD operations on comments.
  - Ability to publish or unpublish posts.
- **TestDriveBooking Manager**:
  - CRUD operations on test drive bookings.
  - Can approve or cancel bookings.


  





