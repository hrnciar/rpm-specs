%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:           nodejs-temp
Version:        0.8.3
Release:        9%{?dist}
Summary:        Temporary files and directories for Node.js
License:        MIT
URL:            https://github.com/bruce/node-temp
Source0:        https://registry.npmjs.org/temp/-/temp-%{version}.tgz
BuildArch:      noarch

%if 0%{?fedora} >= 19
ExclusiveArch:  %{nodejs_arches} noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(os-tmpdir)
BuildRequires:  npm(rimraf)
%endif

%description
This Node.js module handles generating a unique file/directory name under the
appropriate system temporary directory, changing the file to an appropriate
mode, and supports automatic removal.

It has a similar API to the fs module.


%prep
%setup -q -n package
%nodejs_fixdep rimraf "^2.2.6"


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/temp
cp -pr package.json lib/ \
    %{buildroot}%{nodejs_sitelib}/temp
%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%__nodejs test/temp-test.js
%endif


%files
%doc README.md examples/
%license LICENSE
%{nodejs_sitelib}/temp


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 17 2016 Tom Hughes <tom@compton.nu> - 0.8.3-1
- Update to 0.8.3 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.7.0-1
- update to upstream release 0.7.0

* Sun Feb 23 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.6.0-1
- update to upstream release 0.6.0
- apply patch to use native os.tmpDir instead of npm(osenv)

* Tue Jul 30 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.0-3
- update to upstream release 0.5.1
- restrict to compatible arches

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.5.0-2
- rebuild for missing npm(temp) provides on EL6

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.0-1
- initial package
