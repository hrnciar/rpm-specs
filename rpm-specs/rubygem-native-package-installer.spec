%global	gem_name	native-package-installer

Name:		rubygem-%{gem_name}
Version:	1.0.9
Release:	3%{?dist}
Summary:	Native packages installation helper

License:	LGPLv3+
URL:		https://github.com/ruby-gnome2/native-package-installer
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(test-unit-rr)

BuildArch:		noarch

%description
Users need to install native packages to install an extension library
that depends on native packages. It bores users because users need to
install native packages and an extension library separately.
native-package-installer helps to install native packages on "gem install".
Users can install both native packages and an extension library by one action,
"gem install".

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:		noarch

%description	doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Rakefile \
	test/ \
	%{nil}
popd

%check
pushd .%{gem_instdir}
ruby -Ilib:.:test test/run-test.rb
popd

%files
%license	%{gem_instdir}/doc/text/*gpl*txt
%dir	%{gem_instdir}
%dir	%{gem_instdir}/doc
%dir	%{gem_instdir}/doc/text
%doc	%{gem_instdir}/doc/text/*.md
%doc	%{gem_instdir}/README.md

%{gem_libdir}
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.9-1
- 1.0.9

* Thu Oct 17 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.8-1
- 1.0.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr  5 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.7-1
- 1.0.7

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Dec  5 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.6-1
- 1.0.6

* Sun Dec  3 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.5-1
- 1.0.5

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun  5 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.4-1
- 1.0.4

* Mon May 29 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.3-1
- 1.0.3

* Wed May  3 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.1-1
- 1.0.1

* Sun Apr 30 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.0.0-1
- Initial package
