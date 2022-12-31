$("form[name=signup_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/login";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=detail_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/profile",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=login_form").submit(function(e) {
  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/dashboard";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=scrape").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/dashboard",
    type: "GET",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/scrapped";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});


$("form[name=form_scrapped").submit(function(e) {
  var $form = $(this);
  var $error = $form.find(".error");
  $error.text("Scraping the Twitter...").removeClass("error--hidden").css('color', 'green')
  var data = $form.serialize();
  $.ajax({
    url: "/dashboard/scrapped",
    type: "GET",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/annotate";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden").css('color', 'red');
    }
  });

  e.preventDefault();
});

