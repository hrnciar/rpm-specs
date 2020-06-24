%global enable_tests 1

Name:       nodejs-showdown
Version:    0.5.4
Release:    7%{?dist}
Summary:    A JavaScript port of the original Perl version of Markdown
License:    BSD
URL:        https://github.com/coreyti/showdown
Source0:    https://registry.npmjs.org/showdown/-/showdown-%{version}.tgz

BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  nodejs-packaging
#BuildRequires:  npm(grunt-cli)
#BuildRequires:  npm(grunt-contrib-concat)
#BuildRequires:  npm(grunt-contrib-uglify)
#BuildRequires:  npm(grunt-simple-mocha)

%if 0%{?enable_tests}
BuildRequires:  npm(mocha)
BuildRequires:  npm(should)
%endif

%description
%{summary}.


%prep
%autosetup -n package
# Fix wrong-file-end-of-line-encoding rpmlint warnings.
sed -i -e 's/\r//' license.txt example/showdown-gui.js README.md example/syntax.txt
#rm -rf compressed

%build
#%%nodejs_symlink_deps --build
#grunt


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/showdown
cp -pr package.json compressed/ src/ \
    %{buildroot}%{nodejs_sitelib}/showdown

%nodejs_symlink_deps


%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{nodejs_sitelib}/mocha/bin/mocha --require should --ui bdd
%endif


%files
%doc README.md example/
%license license.txt
%{nodejs_sitelib}/showdown


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 19 2017 Piotr Popieluch <piotr1212@gmail.com> - 0.5.4-1
- Update to latest 0.x release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jul 29 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.1-5
- restrict to compatible arches
- enable tests

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.1-4
- rebuild for missing npm(showdown) provides on EL6

* Sat Mar 09 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.1-3
- fix wrong-file-end-of-line-encoding rpmlint warnings

* Sun Feb 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.1-2
- amend mocha options

* Sun Feb 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.1-1
- initial package
