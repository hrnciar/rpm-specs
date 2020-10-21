%{?nodejs_find_provides_and_requires}

Name:       nodejs-cli
Version:    0.5.0
Release:    12%{?dist}
Summary:    Node.js module for rapidly building command line apps
# License text is included in README.md
License:    MIT
URL:        https://github.com/chriso/cli
Source0:    http://registry.npmjs.org/cli/-/cli-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%description
cli is a toolkit for rapidly building command line apps. It includes:

 - Full featured options/arguments parser
 - Plugin support for adding common options and switches
 - Helper methods for working with input/output and spawning child processes
 - Output colored/styled messages, progress bars or spinners
 - Command auto-completion and glob support


%prep
%setup -q -n package
find . -type f -exec chmod 0644 '{}' \;


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/cli
cp -pr package.json cli.js index.js \
    %{buildroot}%{nodejs_sitelib}/cli

%nodejs_symlink_deps


%files
%doc README.md examples/
%{nodejs_sitelib}/cli


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 26 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.5.0-1
- update to upstream release 0.5.0

* Mon Aug 26 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.5-1
- update to upstream release 0.4.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 06 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.4.2-5
- fix compatible arches for f18/el6

* Fri Jul 05 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.4.2-4
- restrict to compatible arches

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.4.2-3
- rebuild to fix npm(cli) provides on EL6

* Sat Mar 23 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.4.2-2
- fix a few more file permissions

* Sat Mar 23 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.4.2-1
- fix file permissions in examples/ directory

* Wed Feb 13 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.4.4-1
- initial package
