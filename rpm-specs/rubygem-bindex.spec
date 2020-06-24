# Generated from bindex-0.5.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name bindex

Name: rubygem-%{gem_name}
Version: 0.5.0
Release: 13%{?dist}
Summary: Bindings for your Ruby exceptions
License: MIT
URL: https://github.com/gsamokovarov/bindex
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel >= 2.0.0
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
BuildRequires: rubygem(minitest)

%description
Bindings for your Ruby exceptions.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}/%{gem_name}
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/%{gem_name}/*.so %{buildroot}%{gem_extdir_mri}/%{gem_name}

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/


%check
pushd .%{gem_instdir}
ruby -I$(dirs +1)%{gem_extdir_mri}:lib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE.txt
%exclude %{gem_instdir}/bindex.gemspec
%{gem_libdir}
%exclude %{gem_libdir}/bindex/*.jar
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Vít Ondruch <vondruch@redhat.com> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.5.0-6
- Rebuilt for switch to libxcrypt

* Wed Jan 03 2018 Vít Ondruch <vondruch@redhat.com> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.5

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 07 2017 Vít Ondruch <vondruch@redhat.com> - 0.5.0-2
- Install binary extension into proper location.

* Thu Apr 06 2017 Vít Ondruch <vondruch@redhat.com> - 0.5.0-1
- Initial package
