%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       nodejs-uglify-to-browserify
Version:    1.0.2
Release:    12%{?dist}
Summary:    A transform to make UglifyJS work in browserify
License:    MIT
URL:        https://github.com/ForbesLindesay/uglify-to-browserify
Source0:    http://registry.npmjs.org/uglify-to-browserify/-/uglify-to-browserify-%{version}.tgz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging

%if 0%{?enable_tests}
BuildRequires:  npm(source-map)
BuildRequires:  uglify-js
%endif

%description
%{summary}.


%prep
%setup -q -n package
for i in LICENSE README.md; do
    sed -i -e 's/\r$//' ${i}
done


%build
#nothing to do


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/uglify-to-browserify
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/uglify-to-browserify

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
%nodejs_symlink_deps --check
%__nodejs test/index.js
%endif


%files
%doc LICENSE README.md
%{nodejs_sitelib}/uglify-to-browserify


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 15 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.2-2
- fix wrong-file-end-of-line-encoding

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.0.2-1
- initial package
