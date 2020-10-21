Name:       js-respond
Version:    1.4.2
Release:    8%{?dist}
Summary:    A fast & lightweight polyfill for min/max-width CSS3 Media Queries
License:    MIT
URL:        https://github.com/scottjehl/Respond
Source0:    https://github.com/scottjehl/Respond/archive/%{version}/respond-%{version}.tar.gz
BuildArch:  noarch

BuildRequires:  web-assets-devel
BuildRequires:  nodejs-packaging
BuildRequires:  npm(grunt) >= 0.4.0
BuildRequires:  npm(grunt-cli) >= 0.1
# Review request : https://bugzilla.redhat.com/show_bug.cgi?id=1364643
#BuildRequires:  npm(grunt-contrib-jshint) >= 0.2.0
# Not packaged yet...
#BuildRequires:  npm(grunt-contrib-qunit) >= 0.3.0
BuildRequires:  npm(grunt-contrib-uglify) >= 0.2.7

Requires:  web-assets-filesystem


%description
The goal of this script is to provide a fast and lightweight (3kb minified /
1kb gzipped) script to enable responsive web designs in browsers that don't
support CSS3 Media Queries - in particular, Internet Explorer 8 and under.
It's written in such a way that it will probably patch support for other
non-supporting browsers as well.


%prep
%setup -q -n Respond-%{version}
rm -f dest/*


%build
%nodejs_symlink_deps --build
grunt uglify
# default is an alias for "jshint", "uglify" tasks.


%install
mkdir -p %{buildroot}%{_jsdir}/
cp -p dest/* %{buildroot}%{_jsdir}/


%files
%license LICENSE-MIT
%doc README.md
%{_jsdir}/respond*.js


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Xavier Bachelot <xavier@bachelot.org> - 1.4.2-1
- Initial package.
