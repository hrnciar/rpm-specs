%{?nodejs_find_provides_and_requires}

%global enable_tests 1

Name:       nodejs-constantinople
Version:    2.0.0
Release:    15%{?dist}
Summary:    Determine whether a JavaScript expression evaluates to a constant
License:    MIT
URL:        https://github.com/ForbesLindesay/constantinople
Source0:    http://registry.npmjs.org/constantinople/-/constantinople-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  mocha
BuildRequires:  uglify-js
%endif

%description
%{summary}.


%prep
%setup -q -n package
find . -type f -exec chmod -x '{}' \;
for i in LICENSE README.md; do
    sed -i -e 's/\r$//' "${i}"
done

%nodejs_fixdep uglify-js '^2.2'


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/constantinople
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/constantinople

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
if [ ! -d node_modules/uglify-js ]; then
    ln -sf /usr/lib/node_modules/uglify-js node_modules/uglify-js
fi
/usr/bin/mocha -R spec
%endif


%files
%doc LICENSE README.md
%{nodejs_sitelib}/constantinople


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Tom Hughes <tom@compton.nu> - 2.0.0-12
- Enable tests

* Thu Jul 19 2018 Tom Hughes <tom@compton.nu> - 2.0.0-11
- Update npm(uglify-js) dependency

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 03 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.0.0-3
- fix symlinks when running tests

* Mon Mar 03 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.0.0-2
- fix symlinks when running tests

* Sun Mar 02 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.0.0-1
- initial package
