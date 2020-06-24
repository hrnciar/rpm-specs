%{?nodejs_find_provides_and_requires}

# no tap? no problem
%global bootstrap 0

Name:           nodejs-optimist
Version:        0.6.1
Release:        8%{?dist}
Summary:        Light-weight option parsing for Node.js
BuildArch:      noarch

# no license file included; package.json says "MIT/X11"
License:        MIT/X11
URL:            https://github.com/substack/node-optimist
Source0:        https://registry.npmjs.org/optimist/-/optimist-%{version}.tgz
Patch0:         fix-tests.patch

BuildRequires:  nodejs-packaging

%if !0%{?bootstrap}
BuildRequires:  npm(tap)
BuildRequires:  npm(hashish)
BuildRequires:  npm(wordwrap)
%endif

%description
Light-weight option parsing with an argv hash. No optstrings attached.

%prep
%setup -q -n package
%patch0 -p0

%nodejs_fixdep wordwrap
%nodejs_fixdep minimist

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/optimist
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/optimist

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if !0%{?bootstrap}
tap test/*.js
%endif

%files
%{nodejs_sitelib}/optimist
%doc readme.markdown example
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 17 2016 Jared Smith <jsmith@fedoraproject.org> - 0.6.1-1
- Update to upstream 0.6.1 release
- Relax version of npm(minimist)

* Tue Feb 16 2016 Jared Smith <jsmith@fedoraproject.org> - 0.4.0-7
- Relax version of npm(wordwrap)

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 0.4.0-6
- cleanup spec
- enable test
- symlink the deps in install

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.4.0-1
- new upstream release 0.4.0

* Fri Jan 18 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.5-1
- initial package generated by npm2rpm