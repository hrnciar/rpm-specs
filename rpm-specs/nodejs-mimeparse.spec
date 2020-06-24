%{?nodejs_find_provides_and_requires}

Name:       nodejs-mimeparse
Version:    0.1.4
Release:    12%{?dist}
Summary:    A Node.js module with basic functions for handling mime-types
License:    MIT
URL:        https://github.com/kriskowal/mimeparse
Source0:    http://registry.npmjs.org/mimeparse/-/mimeparse-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
This Node.js module provides basic functions for handling mime-types. It can
handle matching mime-types against a list of media-ranges. See section
14.1 of the HTTP specification [RFC 2616] for a complete explanation:
<http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.1>


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/mimeparse
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/mimeparse

%nodejs_symlink_deps


%files
%doc CHANGES LICENSE README
%{nodejs_sitelib}/mimeparse


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Jul 27 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.4-2
- restrict to compatible arches

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.4-1
- initial package
