# test
%global enablejit 1

# This component depends on ancient and super-abandoned things.
%global gtkopengl 0

Name:		gambas3
Summary:	IDE based on a basic interpreter with object extensions
Version:	3.14.3
Release:	4%{?dist}
License:	GPL+
URL:		http://gambas.sourceforge.net/
Source0:	https://gitlab.com/gambas/gambas/-/archive/%{version}/gambas-%{version}.tar.bz2
Source1:	%{name}.desktop
BuildRequires:	gcc, gcc-c++
BuildRequires:	automake, autoconf, SDL-devel, SDL_mixer-devel
BuildRequires:	SDL2-devel, SDL2_mixer-devel, SDL2_image-devel, SDL2_ttf-devel
BuildRequires:	mariadb-connector-c-devel, libpq-devel, postgresql-server-devel
BuildRequires:	gtk2-devel, gtk3-devel
BuildRequires:	desktop-file-utils, gettext-devel, curl-devel, librsvg2-devel
BuildRequires:	poppler-devel, bzip2-devel, zlib-devel, pkgconfig
BuildRequires:	unixODBC-devel, libXtst-devel, sqlite-devel, mesa-libGL-devel
BuildRequires:	mesa-libGLU-devel, libpng-devel, libjpeg-devel, libxml2-devel
BuildRequires:	libxslt-devel, pcre-devel, SDL_image-devel, libICE-devel
BuildRequires:	libXcursor-devel, libXft-devel, libtool-ltdl-devel
BuildRequires:	xdg-utils, glibc-devel, libffi-devel
BuildRequires:	cairo-devel, qt4-devel, dbus-devel, libXcursor-devel
BuildRequires:	SDL_ttf-devel, sqlite2-devel, glew-devel
BuildRequires:	imlib2-devel, qt-webkit-devel, gsl-devel
BuildRequires:	libtool, ncurses-devel
BuildRequires:  gmime-devel, libgnome-keyring-devel
BuildRequires:	qt5-qtsvg-devel, qt5-qtbase-devel, qt5-qtx11extras-devel, qt5-qtwebkit-devel
# We need this since linux/videodev.h is dead
BuildRequires:	libv4l-devel
BuildRequires:	openssl-devel, gmp-devel, glew-devel
BuildRequires:	gstreamer1-plugins-base-devel gstreamer1-devel
BuildRequires:	openal-soft-devel, alure-devel
BuildRequires:	pkgconfig(x11), pkgconfig(gl)
# Something on arm is pulling this in...
BuildRequires:	dumb-devel
BuildRequires:	fluidsynth-devel
%if %{gtkopengl}
BuildRequires:	gtkglext-devel
%endif

Patch1:		%{name}-3.12.2-nolintl.patch
Patch2:		%{name}-3.12.2-noliconv.patch
Patch4:		%{name}-3.13.0-poppler-0.73.0.patch
Patch5:		%{name}-3.14.1-gst1.patch
Patch6:		%{name}-3.14.3-printf.patch

%description
Gambas3 is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic (but it is NOT a clone !).
With Gambas3, you can quickly design your program GUI, access MySQL/MariaDB
or PostgreSQL databases, pilot KDE applications with DCOP, translate your
program into many languages, create network applications easily, and so
on...

%package runtime
Summary:	Runtime environment for Gambas3
Provides:	%{name}-gb-gui = %{version}-%{release}
Obsoletes:	%{name}-gb-gui >= 3.3.3

%description runtime
Gambas3 is a free development environment based on a Basic interpreter
with object extensions, like Visual Basic. This package contains the
runtime components necessary to run programs designed in Gambas3.

%package devel
Summary:	Development environment for Gambas3
Requires:	%{name}-runtime = %{version}-%{release}

%description devel
The gambas3-devel package contains the tools needed to compile Gambas3
projects without having to install the complete development environment
(gambas3-ide).

%package scripter
Summary:	Scripter program that allows the creation of Gambas3 scripts
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description scripter
This package includes the scripter program that allows the user to
write script files in Gambas.

%package ide
Summary:	The complete Gambas3 Development Environment
License:	GPL+
Provides:	%{name} = %{version}-%{release}
Requires:	tar, gzip, rpm-build, gettext
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gb-args = %{version}-%{release}
Requires:	%{name}-gb-cairo = %{version}-%{release}
Requires:	%{name}-gb-chart = %{version}-%{release}
Requires:	%{name}-gb-clipper = %{version}-%{release}
Requires:	%{name}-gb-complex = %{version}-%{release}
Requires:	%{name}-gb-compress = %{version}-%{release}
Requires:	%{name}-gb-crypt = %{version}-%{release}
Requires:	%{name}-gb-data = %{version}-%{release}
Requires:	%{name}-gb-db = %{version}-%{release}
Requires:	%{name}-gb-db-form = %{version}-%{release}
Requires:	%{name}-gb-db-mysql = %{version}-%{release}
Requires:	%{name}-gb-db-odbc = %{version}-%{release}
Requires:	%{name}-gb-db-postgresql = %{version}-%{release}
Requires:	%{name}-gb-db-sqlite2 = %{version}-%{release}
Requires:	%{name}-gb-db-sqlite3 = %{version}-%{release}
Requires:	%{name}-gb-dbus = %{version}-%{release}
Requires:	%{name}-gb-desktop = %{version}-%{release}
Requires:	%{name}-gb-desktop-gnome = %{version}-%{release}
Requires:	%{name}-gb-eval-highlight = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}
Requires:	%{name}-gb-form-dialog = %{version}-%{release}
Requires:	%{name}-gb-form-editor = %{version}-%{release}
Requires:	%{name}-gb-form-mdi = %{version}-%{release}
Requires:	%{name}-gb-form-print = %{version}-%{release}
Requires:	%{name}-gb-form-stock = %{version}-%{release}
Requires:	%{name}-gb-form-terminal = %{version}-%{release}
Requires:	%{name}-gb-gmp = %{version}-%{release}
Requires:	%{name}-gb-gsl = %{version}-%{release}
Requires:	%{name}-gb-gtk = %{version}-%{release}
%if %{gtkopengl}
Requires:	%{name}-gb-gtk-opengl = %{version}-%{release}
%else
Provides:	%{name}-gb-gtk-opengl = %{version}-%{release}
Obsoletes:	%{name}-gb-gtk-opengl < 3.14.3-4
%endif
Requires:	%{name}-gb-gtk3 = %{version}-%{release}
Requires:	%{name}-gb-httpd = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}
Requires:	%{name}-gb-image-effect = %{version}-%{release}
Requires:	%{name}-gb-image-imlib = %{version}-%{release}
Requires:	%{name}-gb-image-io = %{version}-%{release}
Requires:	%{name}-gb-inotify = %{version}-%{release}
%if %{enablejit}
Requires:	%{name}-gb-jit = %{version}-%{release}
%else
# This is a lie, but we want to clean it out when we're going.
Provides:	%{name}-gb-jit = %{version}-%{release}
Obsoletes:	%{name}-gb-jit < 3.7.1
%endif
Requires:	%{name}-gb-libxml = %{version}-%{release}
Requires:	%{name}-gb-logging = %{version}-%{release}
Requires:	%{name}-gb-map = %{version}-%{release}
Requires:	%{name}-gb-markdown = %{version}-%{release}
Requires:	%{name}-gb-media = %{version}-%{release}
Requires:	%{name}-gb-media-form = %{version}-%{release}
Requires:	%{name}-gb-memcached = %{version}-%{release}
Requires:	%{name}-gb-mime = %{version}-%{release}
Requires:	%{name}-gb-mysql = %{version}-%{release}
Requires:	%{name}-gb-ncurses = %{version}-%{release}
Requires:	%{name}-gb-net = %{version}-%{release}
Requires:	%{name}-gb-net-curl = %{version}-%{release}
Requires:	%{name}-gb-net-pop3 = %{version}-%{release}
Requires:	%{name}-gb-net-smtp = %{version}-%{release}
Requires:	%{name}-gb-openal = %{version}-%{release}
Requires:	%{name}-gb-opengl = %{version}-%{release}
Requires:	%{name}-gb-opengl-glu = %{version}-%{release}
Requires:	%{name}-gb-opengl-glsl = %{version}-%{release}
Requires:	%{name}-gb-opengl-sge = %{version}-%{release}
Requires:	%{name}-gb-openssl = %{version}-%{release}
Requires:	%{name}-gb-option = %{version}-%{release}
Requires:	%{name}-gb-pcre = %{version}-%{release}
Requires:	%{name}-gb-pdf = %{version}-%{release}
Requires:	%{name}-gb-qt4 = %{version}-%{release}
Requires:	%{name}-gb-qt4-ext = %{version}-%{release}
Requires:	%{name}-gb-qt4-opengl = %{version}-%{release}
Requires:	%{name}-gb-qt4-webkit = %{version}-%{release}
Requires:       %{name}-gb-qt5 = %{version}-%{release}
Requires:	%{name}-gb-qt5-ext = %{version}-%{release}
Requires:       %{name}-gb-qt5-opengl = %{version}-%{release}
Requires:       %{name}-gb-qt5-webkit = %{version}-%{release}
Requires:	%{name}-gb-report = %{version}-%{release}
Requires:	%{name}-gb-report2 = %{version}-%{release}
Requires:	%{name}-gb-scanner = %{version}-%{release}
Requires:	%{name}-gb-sdl = %{version}-%{release}
Requires:	%{name}-gb-sdl-sound = %{version}-%{release}
Requires:	%{name}-gb-sdl2 = %{version}-%{release}
Requires:	%{name}-gb-sdl2-audio = %{version}-%{release}
Requires:	%{name}-gb-settings = %{version}-%{release}
Requires:	%{name}-gb-signal = %{version}-%{release}
Requires:	%{name}-gb-term = %{version}-%{release}
Requires:	%{name}-gb-util = %{version}-%{release}
Requires:	%{name}-gb-util-web = %{version}-%{release}
Requires:	%{name}-gb-v4l = %{version}-%{release}
Requires:	%{name}-gb-vb = %{version}-%{release}
Requires:	%{name}-gb-web = %{version}-%{release}
Requires:	%{name}-gb-web-feed = %{version}-%{release}
Requires:	%{name}-gb-web-form = %{version}-%{release}
Requires:	%{name}-gb-xml = %{version}-%{release}
Requires:	%{name}-gb-xml-html = %{version}-%{release}
Requires:	%{name}-gb-xml-rpc = %{version}-%{release}
Requires:	%{name}-gb-xml-xslt = %{version}-%{release}
# This is a lie, but we need to cleanup
Provides:	%{name}-examples = %{version}-%{release}
Obsoletes:	%{name}-examples <= 3.7.0

%description ide
This package includes the complete Gambas3 Development Environment and the
database manager. Installing this package will give you all of the Gambas3
components.

%package gb-args
Summary:	Gambas3 component package for args
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-args
%{summary}

%package gb-cairo
Summary:	Gambas3 component package for cairo
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-cairo
%{summary}

%package gb-chart
Summary:	Gambas3 component package for chart
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}

%description gb-chart
%{summary}

%package gb-clipper
Summary:	Gambas3 component package for clipper
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-clipper
%{summary}

%package gb-complex
Summary:	Gambas3 component package for complex
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-complex
%{summary}

%package gb-compress
Summary:	Gambas3 component package for compress
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-compress
%{summary}

%package gb-crypt
Summary:	Gambas3 component package for crypt
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-crypt
%{summary}

%package gb-data
Summary:	Gambas3 component package for data
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-data
%{summary}

%package gb-db
Summary:	Gambas3 component package for db
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-db
%{summary}

%package gb-db-form
Summary:	Gambas3 component package for db-form
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}

%description gb-db-form
%{summary}

%package gb-db-mysql
Summary:	Gambas3 component package for db-mysql
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db =	%{version}-%{release}

%description gb-db-mysql
%{summary}

%package gb-db-odbc
Summary:	Gambas3 component package for db-odbc
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db =	%{version}-%{release}

%description gb-db-odbc
%{summary}

%package gb-db-postgresql
Summary:	Gambas3 component package for db-postgresql
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db =	%{version}-%{release}

%description gb-db-postgresql
%{summary}

%package gb-db-sqlite2
Summary:	Gambas3 component package for db-sqlite2
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db =	%{version}-%{release}

%description gb-db-sqlite2
%{summary}

%package gb-db-sqlite3
Summary:	Gambas3 component package for db-sqlite3
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db =	%{version}-%{release}

%description gb-db-sqlite3
%{summary}

%package gb-desktop
Summary:	Gambas3 component package for desktop
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-desktop
%{summary}

%package gb-desktop-gnome
Summary:	Gambas3 component package for GNOME Desktop
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-desktop = %{version}-%{release}

%description gb-desktop-gnome
%{summary}

%package gb-dbus
Summary:	Gambas3 component package for dbus
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-dbus
%{summary}

%package gb-eval-highlight
Summary:	Gambas3 component package for eval highlight
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-eval-highlight
%{summary}

%package gb-form
Summary:	Gambas3 component package for form
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-form
%{summary}

%package gb-form-dialog
Summary:	Gambas3 component package for form-dialog
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}

%description gb-form-dialog
%{summary}

%package gb-form-editor
Summary:        Gambas3 component package for form-editor
Requires:       %{name}-runtime = %{version}-%{release}
Requires:       %{name}-gb-form = %{version}-%{release}

%description gb-form-editor
%{summary}

%package gb-form-mdi
Summary:	Gambas3 component package for form-mdi
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}
Requires:	%{name}-gb-settings = %{version}-%{release}

%description gb-form-mdi
%{summary}

%package gb-form-print
Summary:	Gambas3 component package for form-print
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}

%description gb-form-print
%{summary}

%package gb-form-stock
Summary:	Gambas3 component package for form-stock
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-form-stock
%{summary}

%package gb-form-terminal
Summary:	Gambas3 component package for form-terminal
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-form = %{version}-%{release}

%description gb-form-terminal
%{summary}

%package gb-gmp
Summary:	Gambas3 component package for gmp
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-gmp
%{summary}

%package gb-gsl
Summary:	Gambas3 component package for gsl
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-gsl
%{summary}

%package gb-gtk
Summary:	Gambas3 component package for gtk
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-gtk
%{summary}

%if %{gtkopengl}
%package gb-gtk-opengl
Summary:	Gambas3 component package for gtk-opengl
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-gtk = %{version}-%{release}
Requires:	%{name}-gb-opengl = %{version}-%{release}

%description gb-gtk-opengl
%{summary}
%endif

%package gb-gtk3
Summary:	Gambas3 component package for gtk3
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-gtk3
%{summary}.

%package gb-httpd
Summary:	Gambas3 component package for httpd
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-httpd
%{summary}.

%package gb-image
Summary:	Gambas3 component package for image
License:	GPLv2 or QPL
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-image
%{summary}

%package gb-image-effect
Summary:	Gambas3 component package for image-effect
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}

%description gb-image-effect
%{summary}

%package gb-image-imlib
Summary:	Gambas3 component package for image-imlib
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}

%description gb-image-imlib
%{summary}

%package gb-image-io
Summary:	Gambas3 component package for image-io
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-image = %{version}-%{release}

%description gb-image-io
%{summary}

%package gb-inotify
Summary:	Gambas3 component package for inotify
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-inotify
%{summary}

%if 0%{enablejit}
%package gb-jit
Summary:	Gambas3 component package for jit
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-jit
%{summary}
%endif

%package gb-libxml
Summary:	Gambas3 component package for libxml
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-libxml
%{summary}

%package gb-logging
Summary:	Gambas3 component package for logging
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-logging
%{summary}

%package gb-map
Summary:	Gambas3 component package for map
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-map
%{summary}.

%package gb-markdown
Summary:	Gambas3 component package for markdown
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-markdown
%{summary}.

%package gb-media
Summary:	Gambas3 component package for media
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-media
%{summary}

%package gb-media-form
Summary:	Gambas3 component package for media-form
Requires:	%{name}-gb-media = %{version}-%{release}
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-media-form
%{summary}

%package gb-memcached
Summary:	Gambas3 component package for memcached
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-memcached
%{summary}.

%package gb-mime
Summary:	Gambas3 component package for mime
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-mime
%{summary}

%package gb-mysql
Summary:	Gambas3 component package for mysql
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-db = %{version}-%{release}
Requires:	%{name}-gb-db-mysql = %{version}-%{release}

%description gb-mysql
%{summary}

%package gb-ncurses
Summary:	Gambas3 component package for ncurses
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-ncurses
%{summary}

%package gb-net
Summary:	Gambas3 component package for net
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-net
%{summary}

%package gb-net-curl
Summary:	Gambas3 component package for net.curl
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-net = %{version}-%{release}

%description gb-net-curl
%{summary}

%package gb-net-pop3
Summary:	Gambas3 component package for net-pop3
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-net = %{version}-%{release}
Requires:	%{name}-gb-mime = %{version}-%{release}

%description gb-net-pop3
%{summary}

%package gb-net-smtp
Summary:	Gambas3 component package for net-smtp
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-net-smtp
%{summary}

%package gb-openal
Summary:	Gambas3 component package for openal
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-openal
%{summary}

%package gb-opengl
Summary:	Gambas3 component package for opengl
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-opengl
%{summary}

%package gb-opengl-glu
Summary:	Gambas3 component package for opengl-glu
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-opengl = %{version}-%{release}

%description gb-opengl-glu
%{summary}

%package gb-opengl-glsl
Summary:	Gambas3 component package for opengl-glsl
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-opengl = %{version}-%{release}

%description gb-opengl-glsl
%{summary}

%package gb-opengl-sge
Summary:	Gambas3 component package for opengl-sge
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-opengl = %{version}-%{release}

%description gb-opengl-sge
%{summary}

%package gb-openssl
Summary:	Gambas3 component package for openssl
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-openssl
%{summary}

%package gb-option
Summary:	Gambas3 component package for option
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-option
%{summary}

%package gb-pcre
Summary:	Gambas3 component package for pcre
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-pcre
%{summary}

%package gb-pdf
Summary:	Gambas3 component package for pdf
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-pdf
%{summary}

%package gb-qt4
Summary:	Gambas3 component package for qt4
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-qt4
%{summary}

%package gb-qt4-ext
Summary:	Gambas3 component package for qt4.ext
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt4 = %{version}-%{release}

%description gb-qt4-ext
%{summary}

%package gb-qt4-opengl
Summary:	Gambas3 component package for qt4-opengl
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt4 = %{version}-%{release}
Requires:	%{name}-gb-opengl = %{version}-%{release}

%description gb-qt4-opengl
%{summary}

%package gb-qt4-webkit
Summary:	Gambas3 component package for qt4-webkit
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt4 = %{version}-%{release}

%description gb-qt4-webkit
%{summary}

%package gb-qt5
Summary:        Gambas3 component package for qt5
Requires:       %{name}-runtime = %{version}-%{release}

%description gb-qt5
%{summary}

%package gb-qt5-ext
Summary:	Gambas3 component package for qt5-ext
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-qt5 = %{version}-%{release}

%description gb-qt5-ext
%{summary}

%package gb-qt5-opengl
Summary:        Gambas3 component package for qt5-opengl
Requires:       %{name}-runtime = %{version}-%{release}
Requires:       %{name}-gb-qt5 = %{version}-%{release}
Requires:       %{name}-gb-opengl = %{version}-%{release}

%description gb-qt5-opengl
%{summary}

%package gb-qt5-webkit
Summary:        Gambas3 component package for qt5-webkit
Requires:       %{name}-runtime = %{version}-%{release}
Requires:       %{name}-gb-qt5 = %{version}-%{release}

%description gb-qt5-webkit
%{summary}


%package gb-report
Summary:	Gambas3 component package for report
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-report
%{summary}

%package gb-report2
Summary:	Gambas3 component package for report2
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-report2
%{summary}

%package gb-scanner
Summary:	Gambas3 component package for scanner
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-scanner
%{summary}

%package gb-sdl
Summary:	Gambas3 component package for sdl
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	dejavu-sans-fonts

%description gb-sdl
%{summary}

%package gb-sdl-sound
Summary:	Gambas3 component package for sdl-sound
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-sdl-sound
%{summary}

%package gb-sdl2
Summary:	Gambas3 component for sdl2
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-sdl2
%{summary}

%package gb-sdl2-audio
Summary:	Gambas3 component for sdl2-audio
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-sdl2-audio
%{summary}

%package gb-settings
Summary:	Gambas3 component package for settings
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-settings
%{summary}

%package gb-signal
Summary:	Gambas3 component package for signal
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-signal
%{summary}

%package gb-term
Summary:	Gambas3 component package for term
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-term
%{summary}

%package gb-util
Summary:	Gambas3 component package for util
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-util
%{summary}

%package gb-util-web
Summary:	Gambas3 component package for util web
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-util-web
%{summary}

%package gb-v4l
Summary:	Gambas3 component package for v4l
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-v4l
%{summary}

%package gb-vb
Summary:	Gambas3 component package for vb
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-vb
%{summary}

%package gb-web
Summary:	Gambas3 component package for web
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-web
%{summary}

%package gb-web-feed
Summary:	Gambas3 component package for web-feed
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-web = %{version}-%{release}

%description gb-web-feed
%{summary}

%package gb-web-form
Summary:	Gambas3 component package for web-form
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-web = %{version}-%{release}

%description gb-web-form
%{summary}

%package gb-xml
Summary:	Gambas3 component package for xml
Requires:	%{name}-runtime = %{version}-%{release}

%description gb-xml
%{summary}

%package gb-xml-html
Summary:	Gambas3 component package for xml.html
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-xml = %{version}-%{release}

%description gb-xml-html
%{summary}

%package gb-xml-rpc
Summary:	Gambas3 component package for xml.rpc
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-xml = %{version}-%{release}

%description gb-xml-rpc
%{summary}

%package gb-xml-xslt
Summary:	Gambas3 component package for xml.xslt
Requires:	%{name}-runtime = %{version}-%{release}
Requires:	%{name}-gb-xml = %{version}-%{release}

%description gb-xml-xslt
%{summary}

%prep
%setup -q -n gambas-%{version}
%patch1 -p1 -b .nolintl
%patch2 -p1 -b .noliconv
%patch4 -p1 -b .poppler_0.73.0
%patch5 -p1 -b .gst1
%patch6 -p1 -b .printf
for i in `find . |grep acinclude.m4`; do
	sed -i 's|$AM_CFLAGS -O3|$AM_CFLAGS|g' $i
	sed -i 's|$AM_CXXFLAGS -Os -fno-omit-frame-pointer|$AM_CXXFLAGS|g' $i
	sed -i 's|$AM_CFLAGS -Os|$AM_CFLAGS|g' $i
	sed -i 's|$AM_CFLAGS -O0|$AM_CFLAGS|g' $i
	sed -i 's|$AM_CXXFLAGS -O0|$AM_CXXFLAGS|g' $i
done
# Need this for gcc44
sed -i 's|-fno-exceptions||g' gb.db.sqlite3/acinclude.m4
./reconf-all

# clean up some spurious exec perms
chmod -x main/gbx/gbx_local.h
chmod -x main/gbx/gbx_subr_file.c
chmod -x gb.qt4/src/CContainer.cpp
chmod -x main/lib/option/getoptions.*
chmod -x main/lib/option/main.c

%build
# Gambas can't deal with -Wp,-D_FORTIFY_SOURCE=2
MY_CFLAGS=`echo $RPM_OPT_FLAGS | sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//g'`
%configure \
	--disable-silent-rules \
	--datadir="%{_datadir}" \
	--enable-intl \
	--enable-conv \
	--enable-qt4 \
	--enable-kde \
	--enable-net \
	--enable-curl \
	--enable-postgresql \
	--enable-mysql \
	--enable-sqlite3 \
	--enable-sdl \
	--enable-vb \
	--enable-pdf \
	--with-bzlib2-libraries=%{_libdir} \
	--with-crypt-libraries=%{_libdir} \
	--with-curl-libraries=%{_libdir} \
	--with-desktop-libraries=%{_libdir} \
	--with-ffi-includes=`pkg-config libffi --variable=includedir` \
	--with-ffi-libraries=`pkg-config libffi --variable=libdir` \
	--with-intl-libraries=%{_libdir} \
	--with-conv-libraries=%{_libdir} \
	--with-gettext-libraries=%{_libdir} \
	--with-gtk-libraries=%{_libdir} \
	--with-gtk_svg-libraries=%{_libdir} \
	--with-image-libraries=%{_libdir} \
	--with-kde-libraries=%{_libdir} \
	--with-mysql-includes=%{_includedir}/mysql \
	--with-mysql-libraries=%{_libdir}/mariadb \
	--with-net-libraries=%{_libdir} \
	--with-odbc-libraries=%{_libdir} \
	--with-opengl-libraries=%{_libdir} \
	--with-pcre-libraries=%{_libdir} \
	--with-poppler-libraries=%{_libdir} \
	--with-postgresql-libraries=%{_libdir} \
	--with-qt4-libraries=%{_libdir} \
	--with-qt5-libraries=%{_libdir} \
	--with-qtopengl-libraries=%{_libdir} \
	--with-sdl-libraries=%{_libdir} \
	--with-sdl_sound-libraries=%{_libdir} \
	--with-smtp-libraries=%{_libdir} \
	--with-sqlite2-libraries=%{_libdir} \
	--with-sqlite3-libraries=%{_libdir} \
	--with-v4l-libraries=%{_libdir} \
	--with-xml-libraries=%{_libdir} \
	--with-xslt-libraries=%{_libdir} \
	--with-zlib-libraries=%{_libdir} \
	AM_CFLAGS="$MY_CFLAGS" AM_CXXFLAGS="$MY_CFLAGS" CC="gcc $MY_CFLAGS"
# rpath removal
for i in main; do
	sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' $i/libtool
	sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' $i/libtool
done
# for some unholy reason, using system libtool breaks on qt5. so we don't.
%make_build -C gb.qt5
%make_build

%install
export PATH=%{buildroot}%{_bindir}:$PATH
%make_install
# Why do we have to run this twice? I HAVE NO IDEA.
%make_install

mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/%{name}/examples/
install -m0644 -p ./app/src/%{name}/.icon.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications	\
  %{SOURCE1}

# Get the SVN noise out of the main tree
find %{buildroot}%{_datadir}/%{name}/ -type d -name .svn -exec rm -rf {} 2>/dev/null ';' || :

# Upstream says we don't need those files. Not sure why they install them then. :/
rm -rf %{buildroot}%{_libdir}/%{name}/gb.la %{buildroot}%{_libdir}/%{name}/gb.so*

# No need for the static libs
rm -rf %{buildroot}%{_libdir}/%{name}/*.a

# Mime types.
mkdir -p %{buildroot}%{_datadir}/mime/packages/
install -m 0644 -p app/mime/application-x-gambasscript.xml %{buildroot}%{_datadir}/mime/packages/
install -m 0644 -p main/mime/application-x-gambas3.xml %{buildroot}%{_datadir}/mime/packages/

%files runtime
%doc INSTALL README
%license COPYING
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/gb.component
%{_libdir}/%{name}/gb.debug.*
%{_libdir}/%{name}/gb.draw.*
%{_libdir}/%{name}/gb.eval.*
%{_libdir}/%{name}/gb.geom.*
%{_libdir}/%{name}/gb.gui.*
%{_bindir}/gbr3
%{_bindir}/gbx3
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/template/
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/info/
%{_datadir}/%{name}/info/gb.debug.*
%{_datadir}/%{name}/info/gb.eval.*
%{_datadir}/%{name}/info/gb.gui.*
%{_datadir}/%{name}/info/gb.info
%{_datadir}/%{name}/info/gb.list
%dir %{_datadir}/%{name}/icons/
%{_datadir}/%{name}/icons/application-x-gambas3.png
%{_datadir}/mime/packages/application-x-gambas3.xml
%{_datadir}/%{name}/icons/application-x-gambasserverpage.png

%files devel
%license COPYING
%{_bindir}/gbc3
%{_bindir}/gba3
%{_bindir}/gbh3
%{_bindir}/gbh3.gambas
%{_bindir}/gbi3

%files scripter
%{_bindir}/gbs3
%{_bindir}/gbs3.gambas
%{_bindir}/gbw3
%{_datadir}/%{name}/icons/application-x-gambasscript.png
%{_datadir}/mime/packages/application-x-gambasscript.xml

%files ide
%{_bindir}/%{name}
%{_bindir}/%{name}.gambas
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/metainfo/%{name}.appdata.xml
# The IDE crashes if it can't find this directory.
# Since -examples Requires: -ide, this is okay.
%dir %{_datadir}/%{name}/examples/

%files gb-args
%{_libdir}/%{name}/gb.args.*
%{_datadir}/%{name}/info/gb.args.*

%files gb-cairo
%{_libdir}/%{name}/gb.cairo.*
%{_datadir}/%{name}/info/gb.cairo.*

%files gb-chart
%{_libdir}/%{name}/gb.chart.*
%{_datadir}/%{name}/info/gb.chart.*

%files gb-clipper
%{_libdir}/%{name}/gb.clipper.*
%{_datadir}/%{name}/info/gb.clipper.*

%files gb-complex
%{_libdir}/%{name}/gb.complex.*
%{_datadir}/%{name}/info/gb.complex.*

%files gb-compress
%{_libdir}/%{name}/gb.compress.*
%{_datadir}/%{name}/info/gb.compress.*

%files gb-crypt
%{_libdir}/%{name}/gb.crypt.*
%{_datadir}/%{name}/info/gb.crypt.*

%files gb-data
%{_libdir}/%{name}/gb.data.*
%{_datadir}/%{name}/info/gb.data.*

%files gb-db
%{_libdir}/%{name}/gb.db.component
%{_libdir}/%{name}/gb.db.gambas
%{_libdir}/%{name}/gb.db.la
%{_libdir}/%{name}/gb.db.so*
%{_datadir}/%{name}/info/gb.db.info
%{_datadir}/%{name}/info/gb.db.list

%files gb-db-form
%{_libdir}/%{name}/gb.db.form.*
%{_datadir}/%{name}/control/gb.db.form/
%{_datadir}/%{name}/info/gb.db.form.*

%files gb-db-mysql
%{_libdir}/%{name}/gb.db.mysql.*
%{_datadir}/%{name}/info/gb.db.mysql.*

%files gb-db-odbc
%{_libdir}/%{name}/gb.db.odbc.*
%{_datadir}/%{name}/info/gb.db.odbc.*

%files gb-db-postgresql
%{_libdir}/%{name}/gb.db.postgresql.*
%{_datadir}/%{name}/info/gb.db.postgresql.*

%files gb-db-sqlite2
%{_libdir}/%{name}/gb.db.sqlite2.*
%{_datadir}/%{name}/info/gb.db.sqlite2.*

%files gb-db-sqlite3
%{_libdir}/%{name}/gb.db.sqlite3.*
%{_datadir}/%{name}/info/gb.db.sqlite3.*

%files gb-dbus
%{_libdir}/%{name}/gb.dbus.*
%{_datadir}/%{name}/info/gb.dbus.*

%files gb-desktop
%{_libdir}/%{name}/gb.desktop.*
%exclude %{_libdir}/%{name}/gb.desktop.gnome.*
%{_datadir}/%{name}/control/gb.desktop/
%{_datadir}/%{name}/info/gb.desktop.*

%files gb-desktop-gnome
%{_libdir}/%{name}/gb.desktop.gnome.*

%files gb-eval-highlight
%{_libdir}/%{name}/gb.eval.highlight.*
%{_datadir}/%{name}/info/gb.eval.highlight.*

%files gb-form
%{_libdir}/%{name}/gb.form.component
%{_libdir}/%{name}/gb.form.gambas
%{_datadir}/%{name}/control/gb.form/
%{_datadir}/%{name}/info/gb.form.info
%{_datadir}/%{name}/info/gb.form.list

%files gb-form-dialog
%{_libdir}/%{name}/gb.form.dialog.component
%{_libdir}/%{name}/gb.form.dialog.gambas
%{_datadir}/%{name}/info/gb.form.dialog.info
%{_datadir}/%{name}/info/gb.form.dialog.list

%files gb-form-editor
%{_libdir}/%{name}/gb.form.editor.component
%{_libdir}/%{name}/gb.form.editor.gambas
%{_datadir}/%{name}/control/gb.form.editor/
%{_datadir}/%{name}/info/gb.form.editor.info
%{_datadir}/%{name}/info/gb.form.editor.list

%files gb-form-mdi
%{_libdir}/%{name}/gb.form.mdi.component
%{_libdir}/%{name}/gb.form.mdi.gambas
%{_datadir}/%{name}/control/gb.form.mdi/
%{_datadir}/%{name}/info/gb.form.mdi.info
%{_datadir}/%{name}/info/gb.form.mdi.list

%files gb-form-print
%{_libdir}/%{name}/gb.form.print.component
%{_libdir}/%{name}/gb.form.print.gambas
%{_datadir}/%{name}/info/gb.form.print.info
%{_datadir}/%{name}/info/gb.form.print.list

%files gb-form-stock
%{_libdir}/%{name}/gb.form.stock.component
%{_libdir}/%{name}/gb.form.stock.gambas
%{_datadir}/%{name}/info/gb.form.stock.info
%{_datadir}/%{name}/info/gb.form.stock.list

%files gb-form-terminal
%{_libdir}/%{name}/gb.form.terminal.component
%{_libdir}/%{name}/gb.form.terminal.gambas
%{_datadir}/%{name}/info/gb.form.terminal.info
%{_datadir}/%{name}/info/gb.form.terminal.list
%{_datadir}/%{name}/control/gb.form.terminal/

%files gb-gmp
%{_libdir}/%{name}/gb.gmp.*
%{_datadir}/%{name}/info/gb.gmp.*

%files gb-gsl
%{_libdir}/%{name}/gb.gsl.component
%{_libdir}/%{name}/gb.gsl.so*
%{_libdir}/%{name}/gb.gsl.la
%{_datadir}/%{name}/info/gb.gsl.info
%{_datadir}/%{name}/info/gb.gsl.list

%files gb-gtk
%{_libdir}/%{name}/gb.gtk.component
# %%{_libdir}/%%{name}/gb.gtk.gambas
%{_libdir}/%{name}/gb.gtk.so*
%{_libdir}/%{name}/gb.gtk.la
%{_datadir}/%{name}/info/gb.gtk.info
%{_datadir}/%{name}/info/gb.gtk.list

%if %{gtkopengl}
%files gb-gtk-opengl
%{_libdir}/%{name}/gb.gtk.opengl.component
%{_libdir}/%{name}/gb.gtk.opengl.so*
%{_libdir}/%{name}/gb.gtk.opengl.la
%{_datadir}/%{name}/info/gb.gtk.opengl.info
%{_datadir}/%{name}/info/gb.gtk.opengl.list
%endif

%files gb-gtk3
%{_libdir}/%{name}/gb.gtk3.component
%{_libdir}/%{name}/gb.gtk3.so*
%{_libdir}/%{name}/gb.gtk3.la
%{_datadir}/%{name}/info/gb.gtk3.info
%{_datadir}/%{name}/info/gb.gtk3.list

%files gb-httpd
%{_libdir}/%{name}/gb.httpd.*
%{_datadir}/%{name}/info/gb.httpd.*

%files gb-image
%{_libdir}/%{name}/gb.image.component
%{_libdir}/%{name}/gb.image.so*
%{_libdir}/%{name}/gb.image.la
%{_datadir}/%{name}/info/gb.image.info
%{_datadir}/%{name}/info/gb.image.list

%files gb-image-effect
%{_libdir}/%{name}/gb.image.effect.*
%{_datadir}/%{name}/info/gb.image.effect.*

%files gb-image-imlib
%{_libdir}/%{name}/gb.image.imlib.*
%{_datadir}/%{name}/info/gb.image.imlib.*

%files gb-image-io
%{_libdir}/%{name}/gb.image.io.*
%{_datadir}/%{name}/info/gb.image.io.*

%files gb-inotify
%{_libdir}/%{name}/gb.inotify.component
%{_libdir}/%{name}/gb.inotify.la
%{_libdir}/%{name}/gb.inotify.so*
%{_datadir}/%{name}/info/gb.inotify.info
%{_datadir}/%{name}/info/gb.inotify.list

%if %{enablejit}
%files gb-jit
%{_libdir}/%{name}/gb.jit.*
%{_datadir}/%{name}/info/gb.jit.*
%endif

%files gb-libxml
%{_libdir}/%{name}/gb.libxml.component
%{_libdir}/%{name}/gb.libxml.la
%{_libdir}/%{name}/gb.libxml.so*
%{_datadir}/%{name}/info/gb.libxml.info
%{_datadir}/%{name}/info/gb.libxml.list

%files gb-logging
%{_libdir}/%{name}/gb.logging.*
%{_datadir}/%{name}/info/gb.logging.*

%files gb-map
%{_libdir}/%{name}/gb.map.component
%{_libdir}/%{name}/gb.map.gambas
%{_datadir}/%{name}/info/gb.map.*
%{_datadir}/%{name}/control/gb.map/

%files gb-markdown
%{_libdir}/%{name}/gb.markdown.component
%{_libdir}/%{name}/gb.markdown.gambas
%{_datadir}/%{name}/info/gb.markdown.info
%{_datadir}/%{name}/info/gb.markdown.list

%files gb-media
%{_libdir}/%{name}/gb.media.component
%{_libdir}/%{name}/gb.media.la
%{_libdir}/%{name}/gb.media.so*
%{_datadir}/%{name}/control/gb.media.form/mediaview.png
%{_datadir}/%{name}/info/gb.media.info
%{_datadir}/%{name}/info/gb.media.list

%files gb-media-form
%{_libdir}/%{name}/gb.media.form.component
%{_libdir}/%{name}/gb.media.form.gambas
%{_datadir}/%{name}/info/gb.media.form.info
%{_datadir}/%{name}/info/gb.media.form.list

%files gb-memcached
%{_libdir}/%{name}/gb.memcached.*
%{_datadir}/%{name}/info/gb.memcached.*

%files gb-mime
%{_libdir}/%{name}/gb.mime.*
%{_datadir}/%{name}/info/gb.mime.*

%files gb-mysql
%{_libdir}/%{name}/gb.mysql.*
%{_datadir}/%{name}/info/gb.mysql.*

%files gb-ncurses
%{_libdir}/%{name}/gb.ncurses.component
%{_libdir}/%{name}/gb.ncurses.la
%{_libdir}/%{name}/gb.ncurses.so*
%{_datadir}/%{name}/info/gb.ncurses.info
%{_datadir}/%{name}/info/gb.ncurses.list

%files gb-net
%{_libdir}/%{name}/gb.net.component
%{_libdir}/%{name}/gb.net.so*
%{_libdir}/%{name}/gb.net.la
%{_datadir}/%{name}/info/gb.net.info
%{_datadir}/%{name}/info/gb.net.list

%files gb-net-curl
%{_libdir}/%{name}/gb.net.curl.*
%{_datadir}/%{name}/info/gb.net.curl.*

%files gb-net-pop3
%{_libdir}/%{name}/gb.net.pop3.*
%{_datadir}/%{name}/control/gb.net.pop3/pop3client.png
%{_datadir}/%{name}/info/gb.net.pop3.*

%files gb-net-smtp
%{_libdir}/%{name}/gb.net.smtp.*
%{_datadir}/%{name}/control/gb.net.smtp/smtpclient.png
%{_datadir}/%{name}/info/gb.net.smtp.*

%files gb-openal
%{_libdir}/%{name}/gb.openal.*
%{_datadir}/%{name}/info/gb.openal.*

%files gb-opengl
%{_libdir}/%{name}/gb.opengl.component
%{_libdir}/%{name}/gb.opengl.so*
%{_libdir}/%{name}/gb.opengl.la
%{_datadir}/%{name}/info/gb.opengl.info
%{_datadir}/%{name}/info/gb.opengl.list

%files gb-opengl-sge
%{_libdir}/%{name}/gb.opengl.sge.*
%{_datadir}/%{name}/info/gb.opengl.sge.*

%files gb-opengl-glu
%{_libdir}/%{name}/gb.opengl.glu.*
%{_datadir}/%{name}/info/gb.opengl.glu.*

%files gb-opengl-glsl
%{_libdir}/%{name}/gb.opengl.glsl.*
%{_datadir}/%{name}/info/gb.opengl.glsl.*

%files gb-openssl
%{_libdir}/%{name}/gb.openssl.*
%{_datadir}/%{name}/info/gb.openssl.*

%files gb-option
%{_libdir}/%{name}/gb.option.*
%{_datadir}/%{name}/info/gb.option.*

%files gb-pcre
%{_libdir}/%{name}/gb.pcre.*
%{_datadir}/%{name}/info/gb.pcre.*

%files gb-pdf
%{_libdir}/%{name}/gb.pdf.component
%{_libdir}/%{name}/gb.pdf.so*
%{_libdir}/%{name}/gb.pdf.la
%{_datadir}/%{name}/info/gb.pdf.info
%{_datadir}/%{name}/info/gb.pdf.list

%files gb-qt4
%{_libdir}/%{name}/gb.qt4.component
# %%{_libdir}/%%{name}/gb.qt4.gambas
%{_libdir}/%{name}/gb.qt4.so*
%{_libdir}/%{name}/gb.qt4.la
%{_datadir}/%{name}/info/gb.qt4.info
%{_datadir}/%{name}/info/gb.qt4.list

%files gb-qt4-ext
%{_libdir}/%{name}/gb.qt4.ext.*
%{_datadir}/%{name}/info/gb.qt4.ext.*

%files gb-qt4-opengl
%{_libdir}/%{name}/gb.qt4.opengl.*
%{_datadir}/%{name}/info/gb.qt4.opengl.*

%files gb-qt4-webkit
%{_libdir}/%{name}/gb.qt4.webkit.*
%{_datadir}/%{name}/control/gb.qt4.webkit*
%{_datadir}/%{name}/info/gb.qt4.webkit.*

%files gb-qt5
%{_libdir}/%{name}/gb.qt5.component
# %%{_libdir}/%%{name}/gb.qt5.gambas
%{_libdir}/%{name}/gb.qt5.so*
%{_libdir}/%{name}/gb.qt5.la
%{_datadir}/%{name}/info/gb.qt5.info
%{_datadir}/%{name}/info/gb.qt5.list

%files gb-qt5-ext
%{_libdir}/%{name}/gb.qt5.ext.*
%{_datadir}/%{name}/info/gb.qt5.ext.*

%files gb-qt5-opengl
%{_libdir}/%{name}/gb.qt5.opengl.*
%{_datadir}/%{name}/info/gb.qt5.opengl.*

%files gb-qt5-webkit
%{_libdir}/%{name}/gb.qt5.webkit.*
%{_datadir}/%{name}/control/gb.qt5.webkit*
%{_datadir}/%{name}/info/gb.qt5.webkit.*

%files gb-report
%{_libdir}/%{name}/gb.report.*
%{_datadir}/%{name}/control/gb.report/
%{_datadir}/%{name}/info/gb.report.*

%files gb-report2
%{_libdir}/%{name}/gb.report2.*
%{_datadir}/%{name}/control/gb.report2/
%{_datadir}/%{name}/info/gb.report2.*

%files gb-scanner
%{_libdir}/%{name}/gb.scanner.*
%{_datadir}/%{name}/info/gb.scanner.*

%files gb-sdl
%{_libdir}/%{name}/gb.sdl.component
%{_libdir}/%{name}/gb.sdl.so
%{_libdir}/%{name}/gb.sdl.so.*
%{_libdir}/%{name}/gb.sdl.la
%{_datadir}/%{name}/info/gb.sdl.info
%{_datadir}/%{name}/info/gb.sdl.list
#%%{_datadir}/%%{name}/gb.sdl/

%files gb-sdl-sound
%{_libdir}/%{name}/gb.sdl.sound.*
%{_datadir}/%{name}/info/gb.sdl.sound.*

%files gb-sdl2
%{_libdir}/%{name}/gb.sdl2.component
%{_libdir}/%{name}/gb.sdl2.so
%{_libdir}/%{name}/gb.sdl2.so.*
%{_libdir}/%{name}/gb.sdl2.la
%{_datadir}/%{name}/info/gb.sdl2.info
%{_datadir}/%{name}/info/gb.sdl2.list

%files gb-sdl2-audio
%{_libdir}/%{name}/gb.sdl2.audio.component
%{_libdir}/%{name}/gb.sdl2.audio.so
%{_libdir}/%{name}/gb.sdl2.audio.so.*
%{_libdir}/%{name}/gb.sdl2.audio.la
%{_datadir}/%{name}/info/gb.sdl2.audio.info
%{_datadir}/%{name}/info/gb.sdl2.audio.list

%files gb-settings
%{_libdir}/%{name}/gb.settings.*
%{_datadir}/%{name}/info/gb.settings.*

%files gb-signal
%{_libdir}/%{name}/gb.signal.*
%{_datadir}/%{name}/info/gb.signal.*

%files gb-term
%{_libdir}/%{name}/gb.term.*
%{_datadir}/%{name}/control/gb.term.*
%{_datadir}/%{name}/info/gb.term.*

%files gb-util
%{_libdir}/%{name}/gb.util.component
%{_libdir}/%{name}/gb.util.gambas
%{_datadir}/%{name}/info/gb.util.info
%{_datadir}/%{name}/info/gb.util.list

%files gb-util-web
%{_libdir}/%{name}/gb.util.web.*
%{_datadir}/%{name}/control/gb.util.web/
%{_datadir}/%{name}/info/gb.util.web.*

%files gb-v4l
%{_libdir}/%{name}/gb.v4l.*
%{_datadir}/%{name}/info/gb.v4l.*

%files gb-vb
%{_libdir}/%{name}/gb.vb.*
%{_datadir}/%{name}/info/gb.vb.*

%files gb-web
%{_libdir}/%{name}/gb.web.component
%{_libdir}/%{name}/gb.web.gambas
%{_datadir}/%{name}/info/gb.web.info
%{_datadir}/%{name}/info/gb.web.list

%files gb-web-feed
%{_libdir}/%{name}/gb.web.feed.component
%{_libdir}/%{name}/gb.web.feed.gambas
%{_datadir}/%{name}/info/gb.web.feed.info
%{_datadir}/%{name}/info/gb.web.feed.list

%files gb-web-form
%{_libdir}/%{name}/gb.web.form.component
%{_libdir}/%{name}/gb.web.form.gambas
%{_datadir}/%{name}/info/gb.web.form.info
%{_datadir}/%{name}/info/gb.web.form.list
%{_datadir}/%{name}/control/gb.web.form/

%files gb-xml
%{_libdir}/%{name}/gb.xml.component
%{_libdir}/%{name}/gb.xml.gambas
%{_libdir}/%{name}/gb.xml.so*
%{_libdir}/%{name}/gb.xml.la
%{_datadir}/%{name}/info/gb.xml.info
%{_datadir}/%{name}/info/gb.xml.list

%files gb-xml-html
%{_libdir}/%{name}/gb.xml.html.component
%{_libdir}/%{name}/gb.xml.html.so*
%{_libdir}/%{name}/gb.xml.html.la
%{_datadir}/%{name}/info/gb.xml.html.info
%{_datadir}/%{name}/info/gb.xml.html.list

%files gb-xml-rpc
%{_libdir}/%{name}/gb.xml.rpc.*
%{_datadir}/%{name}/info/gb.xml.rpc.info
%{_datadir}/%{name}/info/gb.xml.rpc.list

%files gb-xml-xslt
%{_libdir}/%{name}/gb.xml.xslt.*
%{_datadir}/%{name}/info/gb.xml.xslt.*

%changelog
* Mon Jun 22 2020 Tom Callaway <spot@fedoraproject.org> - 3.14.3-4
- do not attempt to build/package gb-gtk-opengl (dependencies are ancient and no longer in Fedora)
- fix compile against pgsql 12 (thanks to Honza Horak)

* Tue Jun 16 2020 Tom Callaway <spot@fedoraproject.org> - 3.14.3-3
- rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Tom Callaway <spot@fedoraproject.org> - 3.14.3-1
- update to 3.14.3

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 3.14.2-2
- Rebuild for poppler-0.84.0

* Tue Dec  3 2019 Tom Callaway <spot@fedoraproject.org> - 3.14.2-1
- update to 3.14.2

* Thu Nov 14 2019 Tom Callaway <spot@fedoraproject.org> - 3.14.1-2
- drop gstreamer 0.10

* Tue Oct 29 2019 Tom Callaway <spot@fedoraproject.org> - 3.14.1-1
- Gambas π.1

* Tue Sep 24 2019 Tom Callaway <spot@fedoraproject.org> - 3.14.0-1
- Gambas π!

* Thu Sep 12 2019 Tom Callaway <spot@fedoraproject.org> - 3.13.0-1
- update to 3.13.0

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 3.12.2-3
- Rebuilt for GSL 2.6.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Tom Callaway <spot@fedoraproject.org> - 3.12.2-1
- update to 3.12.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.11.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 25 2019 Marek Kasik <mkasik@redhat.com> - 3.11.4-5
- Rebuild for poppler-0.73.0

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 3.11.4-4
- Rebuilt for libcrypt.so.2 (#1666033)

* Sat Jan 12 2019 Björn Esser <besser82@fedoraproject.org> - 3.11.4-3
- Add patch to fix missing FALSE/TRUE defines
- Remove trailing white-spaces
- Install COPYING using %%license
- Remove unused patches from repo
- Drop unneeded Group tag
- Use %%make_build and %%make_install macros
- Remove unneeded scriptlets, mime-info has file-triggers

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 3.11.4-2
- Rebuilt for glew 2.1.0

* Wed Aug 15 2018 Tom Callaway <spot@fedoraproject.org> - 3.11.4-1
- update to 3.11.4

* Tue Aug 14 2018 Marek Kasik <mkasik@redhat.com> - 3.11.3-2
- Rebuild for poppler-0.67.0

* Mon Jul 23 2018 Tom Callaway <spot@fedoraproject.org> - 3.11.3-1
- update to 3.11.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Marek Kasik <mkasik@redhat.com> - 3.10.0-11
- Rebuild for poppler-0.63.0

* Wed Feb 14 2018 David Tardon <dtardon@redhat.com> - 3.10.0-10
- rebuild for poppler 0.62.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 3.10.0-8
- Rebuilt for switch to libxcrypt

* Wed Nov 08 2017 David Tardon <dtardon@redhat.com> - 3.10.0-7
- rebuild for poppler 0.61.0

* Sat Oct 28 2017 Tom Callaway <spot@fedoraproject.org> - 3.10.0-6
- mariadb fixes (bz1494084)

* Fri Oct 06 2017 David Tardon <dtardon@redhat.com> - 3.10.0-5
- rebuild for poppler 0.60.1

* Fri Sep 08 2017 David Tardon <dtardon@redhat.com> - 3.10.0-4
- rebuild for poppler 0.59.0

* Thu Aug 03 2017 David Tardon <dtardon@redhat.com> - 3.10.0-3
- rebuild for poppler 0.57.0

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Tom Callaway <spot@fedoraproject.org> - 3.10.0-1
- update to 3.10.0

* Thu Jul 13 2017 Tom Callaway <spot@fedoraproject.org> - 3.9.2-8
- rebuild for new mariadb

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Tue Mar 28 2017 David Tardon <dtardon@redhat.com> - 3.9.2-6
- rebuild for poppler 0.53.0

* Tue Feb 21 2017 Tom Callaway <spot@fedoraproject.org> - 3.9.2-5
- fix SDL2 pkg-config detection caused by misquoting

* Mon Feb 20 2017 Tom Callaway <spot@fedoraproject.org> - 3.9.2-4
- apply upstream fix for gcc7 compile fail

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Tom Callaway <spot@fedoraproject.org> - 3.9.2-2
- rebuild for new GLEW

* Tue Jan  3 2017 Tom Callaway <spot@fedoraproject.org> - 3.9.2-1
- update to 3.9.2

* Fri Dec 16 2016 David Tardon <dtardon@redhat.com> - 3.9.1-5
- rebuild for poppler 0.50.0

* Thu Nov 24 2016 Orion Poplawski <orion@cora.nwra.com> - 3.9.1-4
- Rebuild for poppler 0.49.0

* Fri Nov 11 2016 Dan Horák <dan[at]danny.cz> - 3.9.1-3
- drop ExcludeArch

* Fri Oct 21 2016 Marek Kasik <mkasik@redhat.com> - 3.9.1-2
- Rebuild for poppler-0.48.0

* Tue Sep  6 2016 Tom Callaway <spot@fedoraproject.org> - 3.9.1-1
- update to 3.9.1

* Mon Aug 29 2016 Tom Callaway <spot@fedoraproject.org> - 3.9.0-1
- update to 3.9.0

* Mon Jul 18 2016 Marek Kasik <mkasik@redhat.com> - 3.8.4-7
- Rebuild for poppler-0.45.0

* Tue May  3 2016 Marek Kasik <mkasik@redhat.com> - 3.8.4-6
- Rebuild for poppler-0.43.0

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 3.8.4-5
- Rebuild for gsl 2.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 22 2016 Marek Kasik <mkasik@redhat.com> - 3.8.4-3
- Rebuild for poppler-0.40.0

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 3.8.4-2
- Rebuild for glew 1.13

* Tue Dec 15 2015 Tom Callaway <spot@fedoraproject.org> - 3.8.4-1
- update to 3.8.4

* Wed Nov  4 2015 Tom Callaway <spot@fedoraproject.org> - 3.8.3-1
- update to 3.8.3

* Mon Oct  5 2015 Tom Callaway <spot@fedoraproject.org> - 3.8.2-1
- update to 3.8.2

* Wed Sep  9 2015 Tom Callaway <spot@fedoraproject.org> - 3.8.1-1
- update to 3.8.1

* Wed Aug  5 2015 Tom Callaway <spot@fedoraproject.org> - 3.8.0-2
- build qt5 with the generated libtool, everything else with the system libtool

* Tue Aug  4 2015 Tom Callaway <spot@fedoraproject.org> - 3.8.0-1
- update to 3.8.0

* Wed Jul 22 2015 Marek Kasik <mkasik@redhat.com> - 3.7.1-4
- Rebuild (poppler-0.34.0)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Tom Callaway <spot@fedoraproject.org> - 3.7.1-2
- provides/obsoletes the old -examples subpackage

* Mon Apr 13 2015 Tom Callaway <spot@fedoraproject.org> - 3.7.1-1
- update to 3.7.1

* Fri Jan 23 2015 Marek Kasik <mkasik@redhat.com> 3.6.1-3
- Rebuild (poppler-0.30.0)

* Thu Nov 27 2014 Marek Kasik <mkasik@redhat.com> 3.6.1-2
- Rebuild (poppler-0.28.1)

* Tue Nov  4 2014 Tom Callaway <spot@fedoraproject.org> 3.6.1-1
- Update to 3.6.1

* Tue Oct 28 2014 Adam Jackson <ajax@redhat.com> 3.6.0-2
- Rebuild for llvm 3.5

* Wed Oct 15 2014 Adam Jackson <ajax@redhat.com> 3.6.0-1
- Update to 3.6.0

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 3.5.4-3
- update mime scriptlet

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 23 2014 Tom Callaway <spot@fedoraproject.org> - 3.5.4-1
- update to 3.5.4

* Tue Jun 10 2014 Tom Callaway <spot@fedoraproject.org> - 3.5.3-4
- fix llvm-config check to deal with longer version strings

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Marek Kasik <mkasik@redhat.com> 3.5.3-2
- Rebuild (poppler-0.26.0)

* Mon Apr  7 2014 Tom Callaway <spot@fedoraproject.org> 3.5.3-1
- update to 3.5.3

* Wed Jan 15 2014 Dave Airlie <airlied@redhat.com> 3.5.2-2
- rebuild against llvm 3.4

* Mon Jan  6 2014 Tom Callaway <spot@fedoraproject.org> - 3.5.2-1
- update to 3.5.2

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 3.5.1-2
- rebuilt for GLEW 1.10

* Fri Nov  8 2013 Tom Callaway <spot@fedoraproject.org> - 3.5.1-1
- update to 3.5.1
- fix ide requires (bz 1026988)

* Mon Oct 21 2013 Tom Callaway <spot@fedoraproject.org> - 3.5.0-2
- add missing Requires

* Mon Oct 21 2013 Tom Callaway <spot@fedoraproject.org> - 3.5.0-1
- update to 3.5.0

* Mon Aug 19 2013 Marek Kasik <mkasik@redhat.com> - 3.4.2-2
- Rebuild (poppler-0.24.0)

* Fri Aug 16 2013 Tom Callaway <spot@fedoraproject.org> - 3.4.2-1
- update to 3.4.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 24 2013 Marek Kasik <mkasik@redhat.com> 3.4.1-5
- Rebuild (poppler-0.22.5)

* Tue May 28 2013 Adam Jackson <ajax@redhat.com> 3.4.1-4
- Rebuild for final llvm 3.3 soname

* Wed May 08 2013 Adam Jackson <ajax@redhat.com> 3.4.1-3
- Fix build against llvm 3.3

* Mon Apr 08 2013 Jon Ciesla <limburgher@gmail.com> - 3.4.1-2
- Drop desktop vendor tag.

* Mon Apr  1 2013 Tom Callaway <spot@fedoraproject.org> - 3.4.1-1
- update to 3.4.1

* Tue Feb 19 2013 Jens Petersen <petersen@redhat.com> - 3.4.0-2
- f19 rebuild against llvm-3.2

* Thu Feb  7 2013 Tom Callaway <spot@fedoraproject.org> - 3.4.0-1
- update to 3.4.0

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 3.3.4-4
- rebuild due to "jpeg8-ABI" feature drop

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 3.3.4-3
- Rebuild for glew 1.9.0

* Thu Nov 29 2012 Tom Callaway <spot@fedoraproject.org> - 3.3.4-2
- conditionalize the jit subpackage, needs llvm-config >= 3.1,
  which is only in Fedora 18+.

* Wed Nov 28 2012 Tom Callaway <spot@fedoraproject.org> - 3.3.4-1
- update to 3.3.4

* Wed Oct 24 2012 Tom Callaway <spot@fedoraproject.org> - 3.3.3-1
- update to 3.3.3

* Mon Oct  1 2012 Tom Callaway <spot@fedoraproject.org> - 3.3.2-1
- update to 3.3.2

* Mon Sep 24 2012 Tom Callaway <spot@fedoraproject.org> - 3.3.0-1
- update to 3.3.0

* Wed Aug 22 2012 Tom Callaway <spot@fedoraproject.org> - 3.2.1-2
- rebuild to fix broken deps

* Wed Jul 25 2012 Tom Callaway <spot@fedoraproject.org> - 3.2.1-1
- update to 3.2.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Tom Callaway <spot@fedoraproject.org> - 3.2.0-1
- update to 3.2.0

* Mon Jul  2 2012 Marek Kasik <mkasik@redhat.com> - 3.1.1-4
- Rebuild (poppler-0.20.1)

* Tue May 29 2012 Tom Callaway <spot@fedoraproject.org> - 3.1.1-3
- add support for poppler 0.20

* Wed May  2 2012 Tom Callaway <spot@fedoraproject.org> - 3.1.1-2
- add BR: gsl-devel

* Wed May  2 2012 Tom Callaway <spot@fedoraproject.org> - 3.1.1-1
- update to 3.1.1

* Fri Feb 10 2012 Petr Pisar <ppisar@redhat.com> - 3.0.0-2
- Rebuild against PCRE 8.30

* Tue Jan 17 2012 Tom Callaway <spot@fedoraproject.org> - 3.0.0-1
- update to 3.0.0 final

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.99.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.99.6-2
- Rebuild for new libpng

* Fri Nov  4 2011 Tom Callaway <spot@fedoraproject.org> - 2.99.6-1
- update to 2.99.6

* Fri Oct 28 2011 Rex Dieter <rdieter@fedoraproject.org> - 2.99.5-2
- rebuild(poppler)

* Tue Oct 11 2011 Tom Callaway <spot@fedoraproject.org> - 2.99.5-1
- update to 2.99.5

* Fri Sep 30 2011 Marek Kasik <mkasik@redhat.com> - 2.99.4-2
- Rebuild (poppler-0.18.0)

* Mon Sep 26 2011 Tom Callaway <spot@fedoraproject.org> - 2.99.4-1
- 2.99.4

* Tue Sep 20 2011 Marek Kasik <mkasik@redhat.com> - 2.99.3-3
- Rebuild (poppler-0.17.3)

* Wed Sep  7 2011 Tom Callaway <spot@fedoraproject.org> - 2.99.3-2
- make -devel Require -runtime

* Tue Sep  6 2011 Tom Callaway <spot@fedoraproject.org> - 2.99.3-1
- 2.99.3

* Thu Aug 11 2011 Tom Callaway <spot@fedoraproject.org> - 2.99.2-1
- 2.99.2
- clean up exec permissions on gb.sdl/LICENSE

* Tue Aug  9 2011 Tom Callaway <spot@fedoraproject.org> - 2.99.1-3
- disable insecure permissions on example dirs

* Tue Jun  7 2011 Tom Callaway <spot@fedoraproject.org> - 2.99.1-2
- drop kdelibs3-devel BR

* Wed Apr  6 2011 Tom Callaway <spot@fedoraproject.org> - 2.99.1-1
- new package for Gambas3
