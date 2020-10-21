%global gem_name mongoid
# mongodb is no longer in Fedora.
# This package is remaining in Fedora incase someone has 
#   mongodb installed from non-Fedora sources.
# The tests required mongodb, and thus have been removed.

Name: rubygem-%{gem_name}
Version: 7.1.2
Release: 1%{?dist}
Epoch: 1
Summary: Elegant Persistance in Ruby for MongoDB
License: MIT
URL: http://mongoid.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildArch: noarch

%description
Mongoid is an ODM (Object Document Mapper) Framework for MongoDB, written in
Ruby.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
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
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/


%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Fri Aug 21 2020 Troy Dawson <tdawson@redhat.com> - 1:7.1.2-1
- Update to Mongoid 7.1.2 (#1870994)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Troy Dawson <tdawson@redhat.com> - 1:6.1.0-6
- Remove tests because they depended on mongodb
-- https://pagure.io/fesco/issue/2078

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 04 2017 Vít Ondruch <vondruch@redhat.com> - 1:6.1.0-1
- Update to Mongoid 6.1.0.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:3.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 Troy Dawson <tdawson@redhat.com> - 3.1.7-3
- Fix doc / epoch dependency

* Wed Oct 07 2015 Troy Dawson <tdawson@redhat.com> - 3.1.7-2
- Tweek dependencies

* Mon Oct 05 2015 Troy Dawson <tdawson@redhat.com> - 3.1.7-1
- Downgrade to version 3.1.7 (#1257917)
- Epoch added so packages will downgrade

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jul 07 2014 Troy Dawson <tdawson@redhat.com> - 4.0.0-2
- Tweek dependencies

* Mon Jul 07 2014 Troy Dawson <tdawson@redhat.com> - 4.0.0-1
- Updated to version 4.0.0

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 04 2014 Troy Dawson <tdawson@redhat.com> - 3.1.6-1
- Updated to version 3.1.6

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Troy Dawson <tdawson@redhat.com> - 3.1.4-1
- Updated to 3.1.4
- Fixed moped version dependancy problem (#980526)

* Fri May 10 2013 Troy Dawson <tdawson@redhat.com> - 3.1.3-1
- Initial package
