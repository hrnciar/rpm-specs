%global gem_name prawn-icon

Name: rubygem-%{gem_name}
Version: 2.5.0
Release: 3%{?dist}
Summary: Provides icon fonts for PrawnPDF
License: Ruby or GPLv2 or GPLv3
URL: https://github.com/jessedoyle/prawn-icon/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: ruby >= 1.9.3
BuildArch: noarch

%description
Prawn::Icon provides various icon fonts including
FontAwesome, Foundation Icons and GitHub Octicons
for use with the Prawn PDF toolkit.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/README.md
%license %{gem_instdir}/COPYING
%license %{gem_instdir}/GPLv2
%license %{gem_instdir}/GPLv3
%license %{gem_instdir}/LICENSE
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/prawn-icon.gemspec
%{gem_instdir}/spec

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 20 2019 Christopher Brown <chris.brown@redhat.com> - 2.5.0-1
- Update to 2.5.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Christopher Brown <chris.brown@redhat.com> - 2.4.0-1
- Update to 2.4.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 12 2018 Christopher Brown <chris.brown@redhat.com> - 2.3.0-1
- Update to 2.3.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct 29 2016 Fabio Alessandro Locati <fale@redhat.com> - 1.3.0-1
- Update to 1.3.0

* Sat Sep 17 2016 Fabio Alessandro Locati <fale@redhat.com> - 1.2.0-1
- Update to 1.2.0

* Tue Aug 23 2016 Fabio Alessandro Locati <fale@redhat.com> - 1.1.1-1
- Update to 1.1.1

* Fri Jun 17 2016 Fabio Alessandro Locati <fale@redhat.com> - 1.1.0-1
- Initial package
