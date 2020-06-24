%{?nodejs_find_provides_and_requires}

Name:       nodejs-cycle
Version:    1.0.3
Release:    11%{?dist}
Summary:    A Node.js module implementing JSON encoders/decoders in JavaScript
License:    Public Domain
URL:        https://github.com/douglascrockford/JSON-js
Source0:    http://registry.npmjs.org/cycle/-/cycle-%{version}.tgz

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
mkdir -p %{buildroot}%{nodejs_sitelib}/cycle
cp -pr package.json cycle.js \
    %{buildroot}%{nodejs_sitelib}/cycle

%nodejs_symlink_deps


%files
%doc README.md
%{nodejs_sitelib}/cycle


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 18 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.3-1
- update to upstream release 1.0.3

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.2-4
- fix compatible arches for f18/el6

* Fri Jul 05 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.2-3
- restrict to compatible arches

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-2
- rebuild for missing npm(cycle) provides on EL6

* Sat Apr 27 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.2-1
- update to upstream release 1.0.2

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.1-1
- initial package
