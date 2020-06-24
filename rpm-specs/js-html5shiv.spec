Name:       js-html5shiv
Version:    3.7.3
Release:    6%{?dist}
Summary:    Enable use of HTML5 sectioning elements in legacy browsers
License:    MIT or GPLv2
URL:        https://github.com/aFarkas/html5shiv
Source0:    https://github.com/aFarkas/html5shiv/archive/%{version}/html5shiv-%{version}.tar.gz
BuildArch:  noarch

BuildRequires:  web-assets-devel
BuildRequires:  nodejs-packaging
BuildRequires:  npm(grunt) >= 0.4.1
# Not packaged yet...
#BuildRequires:  npm(grunt-bytesize) >= 0.1.0
BuildRequires:  npm(grunt-contrib-watch) >= 0.3.0
BuildRequires:  npm(grunt-contrib-copy) >= 0.4.0
BuildRequires:  npm(grunt-contrib-uglify) >= 0.2.7
Requires:  web-assets-filesystem


%description
The HTML5 Shiv enables use of HTML5 sectioning elements in legacy Internet
Explorer and provides basic HTML5 styling for Internet Explorer 6-9, Safari 4.x
(and iPhone 3.x), and Firefox 3.x.


%prep
%setup -q -n html5shiv-%{version}
rm -f dist/*


%build
%nodejs_symlink_deps --build
#grunt default
#default is an alias for "copy", "uglify", "bytesize", "watch" tasks.
# npm(grunt-bytesize) package is missing...
# watch never ends...
grunt copy uglify


%install
mkdir -p %{buildroot}%{_jsdir}/
cp -p dist/* %{buildroot}%{_jsdir}/


%files
%license "MIT and GPL2 licenses.md"
%doc readme.md
%{_jsdir}/html5shiv*.js


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Xavier Bachelot <xavier@bachelot.org> - 3.7.3-1
- Initial package.
