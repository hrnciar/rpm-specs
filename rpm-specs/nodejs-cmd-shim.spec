%{?nodejs_find_provides_and_requires}

Name:           nodejs-cmd-shim
Version:        2.0.2
Release:        7%{?dist}
Summary:        Used to create executable scripts on Windows and Unix

License:        BSD
URL:            https://github.com/ForbesLindesay/cmd-shim
Source0:        http://registry.npmjs.org/cmd-shim/-/cmd-shim-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

#for tests
BuildRequires:  npm(tap)
BuildRequires:  npm(graceful-fs)
BuildRequires:  npm(mkdirp)
BuildRequires:  npm(rimraf)


%description
The cmd-shim used in npm to create executable scripts on Windows, since symlinks
are not suitable for this purpose there.

On Unix systems, you should use a symbolic link instead, but this module
supports creating shell script shims also.


%prep
%setup -q -n package
%nodejs_fixdep graceful-fs "^4.1.2"


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/cmd-shim
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/cmd-shim
%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%tap test/*.js


%files
%doc README.md
%license LICENSE
%{nodejs_sitelib}/cmd-shim


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun May 07 2017 Jared Smith <jsmith@fedoraproject.org> - 2.0.2-1
- Update to upstream 2.0.2 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Tom Hughes <tom@compton.nu> - 2.0.1-2
- Cleanup spec file, removing %%defattr

* Fri Jan  1 2016 Tom Hughes <tom@compton.nu> - 2.0.1-1
- Update to 2.0.1 upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-3
- restrict to compatible arches

* Thu May 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-2
- fix EOL encodings

* Thu May 30 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.0-1
- initial package
