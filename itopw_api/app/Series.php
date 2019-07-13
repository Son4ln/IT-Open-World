<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Series extends Model
{
    protected $table = "series_series";

    protected $fillable = ['avatar', 'name', 'slug', 'creator_id', 'last_modified_by_id'];

    protected $casts = [
    	'created_at' => 'datetime',
    	'updated_at' => 'datetime',
    	//'deleted_at' => 'datetime',
    ];

    public function posts()
    {
    	return $this->belongsToMany('App\Post');
    }
}
