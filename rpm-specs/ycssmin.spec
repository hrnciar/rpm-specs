%{?nodejs_find_provides_and_requires}

Name:       ycssmin
Version:    1.0.1
Release:    15%{?dist}
Summary:    CSS minification tool
License:    BSD
URL:        https://github.com/yui/ycssmin
Source0:    http://registry.npmjs.org/%{name}/-/%{name}-%{version}.tgz

BuildArch:  noarch
BuildRequires:  nodejs-devel
ExclusiveArch:  %{nodejs_arches} noarch

%description
ycssmin is a CSS minification tool.

It was originally based on the css minification tool used inside of YUI 
Compressor, based on code from Stoyan Stefanov and Isaac Schlueter.

%prep
%setup -q -n package

#drop spurious executable bit
chmod 0644 package.json cssmin.js

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr bin cssmin.js package.json %{buildroot}%{nodejs_sitelib}/%{name}

mkdir -p %{buildroot}%{_bindir}
ln -sf ../lib/node_modules/%{name}/bin/cssmin %{buildroot}%{_bindir}/cssmin

%nodejs_symlink_deps

# yet another test framework that's not packaged yet :-(
#%%check
#istanbul cover --print both -- vows --spec ./tests/*.js

%files
%{nodejs_sitelib}/%{name}
%{_bindir}/cssmin
%doc README.md LICENSE

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jun 18 2013 Stephen Gallagher <sgallagh@redhat.com> - 1.0.1-4
- Specify build arches

* Mon May 06 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.1-3
- improve description
- drop spurious executable permissions
- drop EL5isms

* Fri Mar 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.1-2
- typo fix

* Thu Mar 14 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.0.1-1
- initial package
