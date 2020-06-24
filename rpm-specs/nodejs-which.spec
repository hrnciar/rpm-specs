%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:           nodejs-which
Version:        1.3.0
Release:        7%{?dist}
Summary:        A JavaScript implementation of the 'which' command
License:        MIT
URL:            https://github.com/isaacs/node-which
Source0:        https://registry.npmjs.org/which/-/which-%{version}.tgz
# The test files are not included in the npm tarball.
# Source1 is generated by running Source10, which pulls from the upstream
# version control repository.
Source1:        tests-%{version}.tar.bz2
Source10:       dl-tests.sh

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(isexe)

%if 0%{?enable_tests}
BuildRequires:  npm(tap)
BuildRequires:  npm(mkdirp)
BuildRequires:  npm(rimraf)
%endif

%description
%{summary}.


%prep
%setup -q -n package
# setup the tests
%setup -q -T -D -a 1 -n package


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/which
cp -pr bin which.js package.json %{buildroot}%{nodejs_sitelib}/which
mkdir -p %{buildroot}%{_bindir}
ln -sf ../lib/node_modules/which/bin/which %{buildroot}%{_bindir}/which-nodejs
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%__nodejs -e "require('./')"
%if 0%{?enable_tests}
%tap test/*.js
%endif


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/which
%{_bindir}/which-nodejs


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 01 2018 Jared K. Smith <jsmith@fedoraproject.org> - 1.3.0-3
- Fix up bogus dependencies

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Jared Smith <jsmith@fedoraproject.org> - 1.3.0-1
- Update to upstream 1.3.0 release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jul 13 2016 Jared Smith <jsmith@fedoraproject.org> - 1.2.10-1
- Update to upstream 1.2.10 release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Tom Hughes <tom@compton.nu> - 1.2.4-1
- Update to 1.2.4 upstream release

* Fri Jan 22 2016 Tom Hughes <tom@compton.nu> - 1.2.2-1
- Update to 1.2.2 upstream release

* Mon Jan 18 2016 Tom Hughes <tom@compton.nu> - 1.2.1-2
- Update npm(is-absolute) dependency

* Mon Jan 18 2016 Tom Hughes <tom@compton.nu> - 1.2.1-1
- Update to 1.2.1 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.5-8
- restrict to compatible arches

* Fri May  3 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0.5-7
- Fix broken symlink in bindir

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.5-6
- add macro for EPEL6 dependency generation

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jan 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.5-4
- fix symlink to executable
- actually install the executable!
- rename executable to which-nodejs

* Tue Jan 08 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.5-3
- add missing build section

* Mon Dec 31 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.5-2
- Clean up for submission

* Sun Mar 04 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.5-1
- new upstream release 1.0.5

* Fri Feb 10 2012 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.3-1
- new upstream release 1.0.3

* Sun Dec 18 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-2
- add Group to make EL5 happy

* Tue Oct 25 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.2-1
- new upstream release

* Tue Aug 23 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.0-1
- initial package
