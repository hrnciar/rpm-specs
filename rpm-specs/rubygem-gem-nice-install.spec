# Generated from gem-nice-install-0.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gem-nice-install

Summary: A RubyGems plugin that improves gem installation user experience
Name: rubygem-%{gem_name}
Version: 0.3.0
Release: 10%{?dist}
License: MIT
URL: http://github.com/voxik/gem-nice-install
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: rubygems-devel
Requires: ruby(release)
Requires: ruby(rubygems)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A RubyGems plugin that improves gem installation user experience. If binary
extension build fails, it tries to install its development dependencies.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}


%description doc
Documentation for %{name}

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/data
%doc %{gem_instdir}/MIT
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Josef Stribny <jstribny@redhat.com> - 0.3.0-1
- Update to 0.3.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 27 2013 Josef Stribny <jstribny@redhat.com> - 0.2.0-3
- F-19: Rebuild for ruby 2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Josef Strzibny <jstribny@redhat.com> - 0.2.0-1
- Updated to version 0.2.0

* Thu Oct 25 2012 Josef Strzibny <jstribny@redhat.com> - 0.1.0-2
- Removed LANG=en_US.utf8 option from the installation step;
  was needed for RubyGems 1.8, >= 1.8.24 don't need it

* Thu Oct 18 2012 Josef Strzibny <jstribny@redhat.com> - 0.1.0-1
- Initial package
