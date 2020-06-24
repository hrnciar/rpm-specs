Name:           js-jquery2
Version:        2.2.4
Release:        7%{?dist}
Summary:        JavaScript DOM manipulation, event handling, and AJAX library
BuildArch:      noarch

%global ver_x %(echo %{version} | cut -d. -f1)
%global ver_y %(echo %{version} | cut -d. -f2)
%global ver_z %(echo %{version} | cut -d. -f3)

License:        MIT
URL:            https://jquery.com/
Source0:        https://github.com/jquery/jquery/archive/%{version}/jquery-%{version}.tar.gz

# disable gzip-js during build
Patch1:         disable-gzip-js.patch
# backport of XSS bug fix from upstream; upstream fixed in 3.0.0 and newer
Patch2:         xss-fix-b078a62.patch

BuildRequires:  web-assets-devel
BuildRequires:  nodejs-packaging
BuildRequires:  js-sizzle-static

Provides:       jquery = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}

BuildRequires:  nodejs-grunt >= 0.4.4-3
BuildRequires:  npm(shelljs)
BuildRequires:  npm(grunt-cli)
BuildRequires:  npm(grunt-contrib-uglify)
BuildRequires:  npm(load-grunt-tasks)
BuildRequires:  npm(requirejs)
#BuildRequires:  npm(strip-json-comments) # won't work on epel7 branch
BuildRequires:  nodejs-strip-json-comments

Requires:       web-assets-filesystem
# this replaces js-jquery before it was updated to jQuery 3
Obsoletes:      js-jquery < 3

%description
jQuery is a fast, small, and feature-rich JavaScript library. It makes things
like HTML document traversal and manipulation, event handling, animation, and
Ajax much simpler with an easy-to-use API that works across a multitude of
browsers. With a combination of versatility and extensibility, jQuery has
changed the way that millions of people write JavaScript.

%prep
# autosetup doesn't work right on epel7 branch
%setup -qn jquery-%{version}
%patch1 -p1
%patch2 -p1

#remove precompiled stuff
rm -rf dist/* src/sizzle

#put sizzle where jquery expects it
install -Dp %{_jsdir}/sizzle/latest/sizzle.js src/sizzle/dist/sizzle.js


%build
%nodejs_symlink_deps --build
grunt -v 'build:*:*' uglify


# missing dependencies
#%%check
#grunt


%install
%global installdir %{buildroot}%{_jsdir}/jquery

mkdir -p %{installdir}/%{version}
cp -p dist/* %{installdir}/%{version}

mkdir -p %{buildroot}%{_webassetdir}
ln -s ../javascript/jquery %{buildroot}%{_webassetdir}/jquery

ln -s %{version} %{installdir}/%{ver_x}
ln -s %{version} %{installdir}/%{ver_x}.%{ver_y}


%files
%{_jsdir}/jquery
%{_webassetdir}/jquery
%doc AUTHORS.txt CONTRIBUTING.md LICENSE.txt README.md


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 12 2017 Christopher Tubbs <ctubbsii@fedoraproject.org> - 2.2.4-1
- Initial packaging of js-jquery2 (contrib derived from old js-jquery)
