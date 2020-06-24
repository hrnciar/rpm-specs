%{?nodejs_find_provides_and_requires}

# test dependencies fake and far not packaged yet
%global enable_tests 0

Name:           nodejs-form-data
Version:        0.2.0
Release:        11%{?dist}
Summary:        A module to create readable "multipart/form-data" streams

License:        MIT
URL:            https://github.com/form-data/form-data
Source0:        https://github.com/form-data/form-data/archive/0.2/form-data-%{version}.tar.gz
BuildArch:      noarch

%if 0%{?fedora} >= 19
ExclusiveArch:  %{nodejs_arches} noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

BuildRequires:  npm(async)
BuildRequires:  npm(combined-stream)
BuildRequires:  npm(mime-types)

%if 0%{?enable_tests}
BuildRequires:  npm(fake)
BuildRequires:  npm(far)
BuildRequires:  npm(formidable)
BuildRequires:  npm(request)
%endif

%description
A module to create readable "multipart/form-data" streams.  Can be used to
submit forms and file uploads to other web applications.


%prep
%setup -q -n form-data-0.2
%nodejs_fixdep async "^1.5.0"
%nodejs_fixdep mime-types "^2.1.7"
%nodejs_fixdep combined-stream "^1.0.5"


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/form-data
cp -pr package.json lib %{buildroot}%{nodejs_sitelib}/form-data


%check
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"
%if 0%{?enable_tests}
%__nodejs test/run.js
%endif


%files
%doc Readme.md
%license License
%{nodejs_sitelib}/form-data


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Tom Hughes <tom@compton.nu> - 0.2.0-3
- Cleanup spec file, removing %%defattr

* Tue Dec 01 2015 Piotr Popieluch <piotr1212@gmail.com> - 0.2.0-2
- Fixdep combined-stream

* Sat Nov 21 2015 Tom Hughes <tom@compton.nu> - 0.2.0-1
- update to 0.2.0 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 26 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.1-1
- update to upstream release 0.1.1
- add ExclusiveArch logic

* Tue Jul 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.0-1
- new upstream release 0.1.0

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.10-1
- new upstream release 0.0.10

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.7-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.7-2
- add macro for EPEL6 dependency generation

* Wed Feb 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.7-1
- new upstream release 0.0.7
- combined-stream dep good now

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-4
- fix combined-stream dep for 0.0.4

* Sat Feb 09 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-3
- fix async dep for new version

* Mon Jan 14 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-2
- add missing dist macro to Release

* Thu Jan 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.6-1
- new upstream release 0.0.6

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-2
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.0.5-1
- initial package generated by npm2rpm