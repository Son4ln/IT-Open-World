<?php

use Illuminate\Http\Request;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});

Route::apiResources([
    'series' => 'API\SerieController',
]);

Route::get('/serie', 'SerieController@index')->name('serie-index');
Route::get('/serie/{serie}', 'SerieController@show')->name('serie-show');
Route::post('/serie', 'SerieController@store')->name('serie-store');
Route::put('/serie/{serie}', 'SerieController@update')->name('serie-update');
Route::delete('/serie/{serie}', 'SerieController@delete')->name('serie-delete');

Route::get('/category', 'CategoryController@index')->name('category-index');
Route::get('/category/{category}', 'CategoryController@show');
Route::post('/category', 'CategoryController@store')->name('category-store');
Route::put('/category/{category}', 'CategoryController@update')->name('category-update');
Route::delete('/category/{category}', 'CategoryController@delete')->name('category-delete');

Route::get('/post', 'PostController@index')->name('post-index');
Route::get('/post/{post}', 'PostController@show')->name('post-show');
Route::post('/post', 'PostController@store')->name('post-store');
Route::put('/post/{post}', 'PostController@update')->name('post-update');
Route::delete('/post/{post}', 'PostController@delete')->name('post-delete');


