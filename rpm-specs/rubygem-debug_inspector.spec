# Generated from debug_inspector-0.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name debug_inspector

Name: rubygem-%{gem_name}
Version: 0.0.3
Release: 10%{?dist}
Summary: A Ruby wrapper for the MRI 2.0 debug_inspector API
License: MIT
URL: https://github.com/banister/debug_inspector
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
# Compiler is required for build of gem binary extension.
# https://fedoraproject.org/wiki/Packaging:C_and_C++#BuildRequires_and_Requires
BuildRequires: gcc
BuildRequires: rubygem(minitest) >= 5

%description
A Ruby wrapper for the MRI 2.0 debug_inspector API.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

chmod -x %{buildroot}%{gem_dir}/gems/%{gem_name}-%{version}/Rakefile

%check
pushd .%{gem_instdir}
# No real upstream test suite available yet :/ but we can do some smoke test :)
ruby -Ilib:$(dirs +1)%{gem_extdir_mri} - << \EOF | grep '#<Class:RubyVM::DebugInspector>'
  require 'debug_inspector'

  # Open debug context
  # Passed `dc' is only active in a block
  RubyVM::DebugInspector.open { |dc|
    # backtrace locations (returns an array of Thread::Backtrace::Location objects)
    locs = dc.backtrace_locations

    # class of i-th caller frame
    p dc.frame_class(0)
  }
EOF
popd


%files
%doc %{gem_instdir}/README.md
%dir %{gem_instdir}
%{gem_extdir_mri}
%exclude %{gem_instdir}/.travis.yml
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/debug_inspector.gemspec
%{gem_instdir}/test

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Vít Ondruch <vondruch@redhat.com> - 0.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 0.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.0.3-3
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.3-2
- F-28: rebuild for ruby25

* Thu Jan 04 2018 Vít Ondruch <vondruch@redhat.com> - 0.0.3-1
- Update to debug_inspector 0.0.3.

* Thu Jan 04 2018 Vít Ondruch <vondruch@redhat.com> - 0.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.5

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Vít Ondruch <vondruch@redhat.com> - 0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.4

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 07 2016 Vít Ondruch <vondruch@redhat.com> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Vít Ondruch <vondruch@redhat.com> - 0.0.2-2
- Update to recent guidelines + review fixes.

* Mon May 06 2013 Anuj More - 0.0.2-1
- Initial package
