%global commit 4bc009145202d9c7483ba85f3a236a8f3470354d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global jsname jquery-ui-touch-punch

Name:		js-%{jsname}
Version:	0.2.3
Release:	0.6.20141219git%{shortcommit}%{?dist}
Summary:	Touch Event Support for jQuery UI

License:	MIT or GPLv2
URL:		http://touchpunch.furf.com/
Source0:	https://github.com/furf/%{jsname}/archive/%{commit}/%{jsname}-%{version}-%{shortcommit}.tar.gz

BuildArch:	noarch
BuildRequires:	uglify-js
BuildRequires:	web-assets-devel
#		This matches js-jquery1, js-jquery2 or js-jquery
Requires:	jquery >= 1.0
%if %{?fedora}%{!?fedora:0} || %{?rhel}%{!?rhel:0} >= 8
Requires:	xstatic-jquery-ui-common >= 1.0
%else
Requires:	python-XStatic-jquery-ui >= 1.0
%endif
Requires:	web-assets-filesystem

%description
jQuery UI Touch Punch is a small hack that enables the use of touch
events on sites using the jQuery UI user interface library.

%prep
%setup -q -n %{jsname}-%{commit}

# Remove pre-minified script
rm *.min.js

%build
# Minify script
uglifyjs jquery.ui.touch-punch.js -c -m --comments '/^!/' \
      -o jquery.ui.touch-punch.min.js

%install
mkdir -p %{buildroot}/%{_jsdir}/%{jsname}
install -m 644 -p *.js %{buildroot}/%{_jsdir}/%{jsname}

%files
%{_jsdir}/%{jsname}
%doc README.md

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.6.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.5.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.4.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.3.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-0.2.20141219git4bc0091
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec 19 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 0.2.3-0.1.20141219git4bc0091
- First packaging for Fedora
