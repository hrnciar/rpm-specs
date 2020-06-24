%{?nodejs_find_provides_and_requires}
%global enable_tests 0
Name:       nodejs-events
Version:    1.0.2
Release:    10%{?dist}
Summary:    Node's event emitter 
License:    MIT
URL:        https://github.com/Gozala/events
Source:     https://github.com/Gozala/events/archive/v%{version}.tar.gz

BuildArch:  noarch

BuildRequires:  nodejs-packaging
BuildRequires:  npm(mocha)

ExclusiveArch: %{nodejs_arches} noarch

%description
Node's event emitter for node.js

%prep
%setup -q -n events-%{version}

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/nodejs-events
cp -pr events.js package.json \
    %{buildroot}%{nodejs_sitelib}/nodejs-events


%check
%if 0%{?enable_tests}
mocha --ui qunit -- tests/index.js
%endif

%files
%doc LICENSE History.md Readme.md tests/ 
%{nodejs_sitelib}/nodejs-events


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 06 2014 Anish Patil <apatil@redhat.com> - 1.0.2-1
- Initial package
