Name:       nodejs-grunt-git-authors
Version:    1.2.0
Release:    13%{?dist}
Summary:    A Grunt module to generate a list of authors from git history
License:    MIT
URL:        https://github.com/scottgonzalez/grunt-git-authors
Source0:    https://registry.npmjs.org/grunt-git-authors/-/grunt-git-authors-%{version}.tgz

BuildArch:  noarch

ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging

Requires:       git

%description
%{summary}.


%prep
%setup -q -n package
%nodejs_fixdep grunt


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/grunt-git-authors
cp -pr package.json tasks/ \
    %{buildroot}%{nodejs_sitelib}/grunt-git-authors

%nodejs_symlink_deps


%files
%doc README.md
%license LICENSE-MIT
%{nodejs_sitelib}/grunt-git-authors


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 24 2016 Piotr Popieluch <piotr1212@gmail.com> - - 1.2.0-6
- fixdep grunt

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 31 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.0-2
- add Requires: git

* Sat Mar 29 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2.0-1
- initial package
