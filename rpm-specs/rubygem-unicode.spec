%global gem_name unicode

Name:           rubygem-%{gem_name}
Version:        0.4.4.2
Release:        16%{?dist}
Summary:        Unicode normalization library for Ruby
License:        Ruby
URL:            http://www.yoshidam.net/Ruby.html#unicode
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/blackwinter/unicode/issues/7
Source1:        https://www.ruby-lang.org/en/about/license.txt
# This is a C extension linked against MRI, it's not compatible with other 
# interpreters. So we require MRI specifically instead of ruby(release).
Requires:       ruby
BuildRequires:  gcc
BuildRequires:  ruby-devel
BuildRequires:  rubygems-devel
# rubygem Requires/Provides are automatically generated in F21+
%if ! (0%{?fedora} >= 21 || 0%{?rhel} >= 8)
Requires:       rubygems
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
Unicode normalization library for Ruby.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
cp -p %{SOURCE1} .

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/specifications %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_instdir}
cp -pa .%{gem_instdir}/lib %{buildroot}%{gem_instdir}/
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -pa .%{gem_extdir_mri}/%{gem_name} .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
%else
mkdir -p %{buildroot}%{gem_extdir_mri}/lib
mv %{buildroot}%{gem_instdir}/lib/unicode %{buildroot}%{gem_extdir_mri}/lib/
%endif

%check
%if 0%{?rhel}
ruby -I.%{gem_instdir}/lib:.%{gem_extdir_mri} test/test.rb
%else
ruby-mri -I.%{gem_instdir}/lib:.%{gem_extdir_mri} test/test.rb
%endif

%files
%doc README license.txt
%{gem_instdir}
%{gem_extdir_mri}
%{gem_spec}

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.4.2-15
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 0.4.4.2-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.4.4.2-9
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.4.2-8
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Vít Ondruch <vondruch@redhat.com> - 0.4.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Vít Ondruch <vondruch@redhat.com> - 0.4.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Wed Nov 04 2015 Dan Callaghan <dcallagh@redhat.com> - 0.4.4.2-1
- upstream bug fix release 0.4.4.2

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 16 2015 Vít Ondruch <vondruch@redhat.com> - 0.4.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.2

* Fri Jan 09 2015 Dan Callaghan <dcallagh@redhat.com> - 0.4.4.1-3
- RHBZ#1179543 include gem.build_complete file so that rubygems doesn't attempt 
  to rebuild the gem

* Mon Jul 14 2014 Dan Callaghan <dcallagh@redhat.com> - 0.4.4.1-2
- run test program in %%check
- use HTTPS for Ruby license source URL

* Thu Jun 05 2014 Dan Callaghan <dcallagh@redhat.com> - 0.4.4.1-1
- updated to upstream release 0.4.4.1
- fixed spec for rubygem changes in F21+

* Tue Jan 28 2014 Dan Callaghan <dcallagh@redhat.com> - 0.4.4-1
- Initial package
