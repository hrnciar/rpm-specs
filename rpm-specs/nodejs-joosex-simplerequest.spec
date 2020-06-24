%{?nodejs_find_provides_and_requires}

Name:       nodejs-joosex-simplerequest
Version:    0.2.2
Release:    14%{?dist}
Summary:    Simple XHR request abstraction for Node.js
# README.md contains a copy of the BSD license, while LICENSE contains
# a copy of the LGPLv3 license.
License:    BSD or LGPLv3
URL:        https://github.com/SamuraiJack/JooseX-SimpleRequest
Source0:    http://registry.npmjs.org/joosex-simplerequest/-/joosex-simplerequest-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
%{summary}.


%prep
%setup -q -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/joosex-simplerequest
rm -f lib/JooseX/SimpleRequest.mmd
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/joosex-simplerequest

%nodejs_symlink_deps


%files
%doc Changes LICENSE README.md doc/
%{nodejs_sitelib}/joosex-simplerequest


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jan 12 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.2-4
- fix License field (should be 'or' not 'and')

* Sat Jan 11 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.2-3
- re-include LICENSE

* Sat Jan 11 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.2-2
- do not package __script/
- remove extraneous license
- fix License field

* Sun Feb 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.2-1
- initial package
