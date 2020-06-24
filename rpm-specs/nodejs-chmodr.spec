%{?nodejs_find_provides_and_requires}

Name:       nodejs-chmodr
Version:    0.1.0
Release:    16%{?dist}
Summary:    Recursively change UNIX file permissions
License:    BSD
URL:        https://github.com/isaacs/chmodr
Source0:    https://registry.npmjs.org/chmodr/-/chmodr-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
BuildRequires:  npm(tap)
BuildRequires:  npm(rimraf)
BuildRequires:  npm(mkdirp)


%description
%{summary}, like `chmod -R`.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/chmodr
cp -pr chmodr.js package.json %{buildroot}%{nodejs_sitelib}/chmodr

%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
tap test/*

%files
%{nodejs_sitelib}/chmodr
%doc README.md
%license LICENSE

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 07 2016 Piotr Popieluch <piotr1212@gmail.com> - 0.1.0-9
- Cleanup spec
- Enable check

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.0-4
- restrict to compatible arches

* Wed Apr 17 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.0-3
- add macro for EPEL 6 dependency generation

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.0-2
- fix License tag

* Wed Mar 13 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.1.0-1
- initial package
