Name:           jake
Version:        10.3.2
Release:        2%{?dist}
Summary:        The JavaScript build tool for Node.js

License:        ASL 2.0
URL:            http://jakejs.com/
Source0:        http://registry.npmjs.org/jake/-/jake-%{version}.tgz
# https://github.com/jakejs/jake/pull/277
Source1:        http://www.apache.org/licenses/LICENSE-2.0
Patch0:         jake-man.patch
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

BuildRequires:  npm(async)
BuildRequires:  npm(chalk)
BuildRequires:  npm(filelist)
BuildRequires:  npm(q)
BuildRequires:  npm(utilities)

%description
Jake is the JavaScript build tool for NodeJS. Jake has been
around since the very early days of Node, and is very full
featured and well tested.


%prep
%setup -q -n jake-v%{version}
%patch0 -p1
cp %{SOURCE1} LICENSE
%nodejs_fixdep async "^1.5.0"
%nodejs_fixdep chalk "^1.1.1"
%nodejs_fixdep minimatch "^3.0.0"
rm -rf node_modules


%build
chmod a+x bin/cli.js


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/jake
cp -pr package.json bin lib %{buildroot}%{nodejs_sitelib}/jake
mkdir -p %{buildroot}%{_bindir}
ln -s %{nodejs_sitelib}/jake/bin/cli.js %{buildroot}%{_bindir}/jake
mkdir -p %{buildroot}%{_mandir}/man1
cp -pr man/jake.1 %{buildroot}%{_mandir}/man1
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} bin/cli.js test


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/jake
%{_bindir}/jake
%{_mandir}/man1/*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 10.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 24 2019 Tom Hughes <tom@compton.nu> - 10.3.2-1
- Update to 10.3.2 upstream release

* Thu Nov 14 2019 Tom Hughes <tom@compton.nu> - 10.3.1-1
- Update to 10.3.1 upstream release

* Wed Nov  6 2019 Tom Hughes <tom@compton.nu> - 10.1.9-1
- Update to 10.1.9 upstream release

* Thu Oct 31 2019 Tom Hughes <tom@compton.nu> - 10.1.6-1
- Update to 10.1.6 upstream release

* Wed Oct 30 2019 Tom Hughes <tom@compton.nu> - 10.1.5-1
- Update to 10.1.5 upstream release

* Sun Oct 27 2019 Tom Hughes <tom@compton.nu> - 10.1.4-1
- Update to 10.1.4 upstream release

* Sun Oct 27 2019 Tom Hughes <tom@compton.nu> - 10.1.3-1
- Update to 10.1.3 upstream release

* Sun Oct 27 2019 Tom Hughes <tom@compton.nu> - 10.1.2-1
- Update to 10.1.2 upstream release

* Tue Oct 22 2019 Tom Hughes <tom@compton.nu> - 10.1.1-1
- Update to 10.1.1 upstream release

* Fri Oct 18 2019 Tom Hughes <tom@compton.nu> - 10.0.6-1
- Update to 10.0.6 upstream release

* Thu Oct 10 2019 Tom Hughes <tom@compton.nu> - 10.0.3-1
- Update to 10.0.3 upstream release

* Thu Oct 10 2019 Tom Hughes <tom@compton.nu> - 10.0.2-1
- Update to 10.0.2 upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar 17 2019 Tom Hughes <tom@compton.nu> - 8.1.1-1
- Update to 8.1.1 upstream release

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug  5 2018 Tom Hughes <tom@compton.nu> - 8.0.18-1
- Update to 8.0.18 upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Tom Hughes <tom@compton.nu> - 8.0.16-1
- Update to 8.0.16 upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 11 2016 Tom Hughes <tom@compton.nu> - 8.0.15-1
- Update to 8.0.15 upstream release

* Thu Oct  6 2016 Tom Hughes <tom@compton.nu> - 8.0.14-1
- Update to 8.0.14 upstream release

* Mon Feb 22 2016 Tom Hughes <tom@compton.nu> - 8.0.12-5
- Update npm(chalk) dependency

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 8.0.12-3
- Update minimatch dependency

* Sat Nov 21 2015 Tom Hughes <tom@compton.nu> - 8.0.12-2
- Update async dependency

* Wed Aug 26 2015 Tom Hughes <tom@compton.nu> - 8.0.12-1
- Update to 8.0.12 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Nov 25 2014 Tom Hughes <tom@compton.nu> - 8.0.10-3
- Add manual page

* Tue Nov 25 2014 Tom Hughes <tom@compton.nu> - 8.0.10-2
- Remove package name from summary

* Sat Nov 15 2014 Tom Hughes <tom@compton.nu> - 8.0.10-1
- Initial build of 8.0.10
