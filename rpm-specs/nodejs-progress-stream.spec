%bcond_with internet

Name:           nodejs-progress-stream
Version:        2.0.0
Release:        7%{?dist}
Summary:        Read the progress of a stream

License:        BSD
URL:            https://github.com/freeall/progress-stream
Source0:        https://registry.npmjs.org/progress-stream/-/progress-stream-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

%if %{with internet}
BuildRequires:  npm(numeral)
BuildRequires:  npm(request)
BuildRequires:  npm(single-line-log)
BuildRequires:  npm(speedometer)
BuildRequires:  npm(through2)
%endif


%description
Read the progress of a stream. Supports speed and eta.

Gets the lengths of the stream automatically if you're using the request
or http module. You can also pass the length on initiation. Progress-stream
will also check to see if the stream already have a length property.


%prep
%setup -q -n package
rm -rf node_modules


%build


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/progress-stream
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/progress-stream
%nodejs_symlink_deps


%if %{with internet}
%check
%nodejs_symlink_deps --check
%{__nodejs} test/http.js && %{__nodejs} test/request.js || false
%endif


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/progress-stream


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 11 2017 Tom Hughes <tom@compton.nu> - 2.0.0-1
- Update to 2.0.0 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec  2 2015 Tom Hughes <tom@compton.nu> - 1.2.0-1
- Update to 1.2.0 upstream release

* Fri Oct 16 2015 Tom Hughes <tom@compton.nu> - 1.1.1-3
- Fix speedometer dependency

* Sat Sep  5 2015 Tom Hughes <tom@compton.nu> - 1.1.1-2
- Fix through2 dependency

* Wed Aug 26 2015 Tom Hughes <tom@compton.nu> - 1.1.1-1
- Initial build of 1.1.1
