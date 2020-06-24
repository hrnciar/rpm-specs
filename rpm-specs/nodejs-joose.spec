%{?nodejs_find_provides_and_requires}
%global __provides_exclude_from ^%{nodejs_sitelib}/joose/librarian/.*$

%global enable_tests 0

Name:       nodejs-joose
Version:    3.50.0
Release:    13%{?dist}
Summary:    Post modern self-hosting meta object system for JavaScript
# License text is included in README.md
License:    BSD
URL:        https://github.com/Joose/Joose
Source0:    http://registry.npmjs.org/joose/-/joose-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

# The requires that librarian uses are relative paths and need to be fixed.
Patch0:     nodejs-joose-3.50.0-librarian-requires.patch
# The requires that joose uses need to be fixed after moving librarian to a
# different location.
Patch1:     nodejs-joose-3.50.0-joose-requires.patch

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(test-run)
%endif

%description
Post modern self-hosting meta object system for JavaScript with support
for classes, inheritance, roles, traits, method modifiers and more.

%prep
%setup -q -n package
%patch0 -p1
%patch1 -p1
# librarian doesn't appear to be a real module. joose doesn't list librarian
# as a dependency, and librarian doesn't have a package.json, though both
# modules 'require' each other. There is also already another module on the
# npm registry called librarian. To simplify things and reduce confusion, I'm
# going to treat librarian as part of joose itself rather than separating it
# into a subpackage.
mv node_modules/librarian librarian
rm -rf node_modules
%nodejs_fixdep paperboy '~0.0.5'


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/joose
cp -pr package.json \
    joose-all.js joose-all-min.js joose-all-web.js joose-webseed.js \
    lib/ librarian/ \
    %{buildroot}%{nodejs_sitelib}/joose

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%__nodejs t/index.js
%__nodejs node_modules/librarian/t/index.js
%endif


%files
%doc Changes LICENSE README.md doc/
%{nodejs_sitelib}/joose


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.50.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.50.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.50.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.50.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.50.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.50.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.50.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.50.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.50.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.50.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.50.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 21 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.50.0-2
- filter out incorrect Provides

* Sun Feb 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 3.50.0-1
- initial package
