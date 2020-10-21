%global         gem_name ruby-shadow

Name:           rubygem-%{gem_name}
Version:        2.5.0
Release:        13%{?dist}
Summary:        Ruby shadow password module
License:        Public Domain
URL:            https://github.com/apalmblad/ruby-shadow
Source0:        http://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        https://raw.githubusercontent.com/apalmblad/ruby-shadow/master/test/basic_test.rb
Patch0:         ruby-shadow-2.5.0-cflags.patch
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby-devel
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(test-unit)
Obsoletes:      ruby-shadow < 1.4.1-36
Provides:       ruby-shadow = %{version}-%{release}
Provides:       ruby(shadow) = %{version}
%description
This module provides access to shadow passwords on Linux and Solaris.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%patch0 -p0
cp %{SOURCE1} .

%build
export CONFIGURE_ARGS="--with-cflags='%{optflags}'"
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

# two identical so files confuses rpmbuild
find %{buildroot}%{gem_dir}/ -name \*.so -delete

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
cp %{SOURCE1} .%{gem_instdir}
pushd .%{gem_instdir}
if [ $(id -u) = 0 ]; then
    ruby -I. -e 'Dir.glob "*_test.rb", &method(:require)'
else
    ruby -I. -e 'Dir.glob "*_test.rb", &method(:require)' || :
fi
popd

%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/*
%doc %{gem_instdir}/HISTORY
%doc %{gem_instdir}/README
%doc %{gem_instdir}/README.euc

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.0-11
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 17 2019 Vít Ondruch <vondruch@redhat.com> - 2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Sun Jul 15 2018 Terje Rosten <terje.rosten@ntnu.no> - 2.5.0-7
- Add C compiler

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.5.0-4
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.5.0-3
- F-28: rebuild for ruby25

* Mon Oct 09 2017 Terje Rosten <terje.rosten@ntnu.no> - 2.5.0-2
- Remove group
- Run tests

* Thu Oct 05 2017 Terje Rosten <terje.rosten@ntnu.no> - 2.5.0-1
- 2.5.0
- Remove non Fedora support
- Simplify

* Fri Mar 01 2013 Moses Mendoza <moses@puppetlabs.com> - 2.2.0-1
- Update to upstream 2.2.0
- Move gem path macro definitions inside rhel5 macro block
- Install only files we want rather than removing files we dont
- Remove extraneous case in spec for gem_instdir/*.so
- Move gemspec(s) into docs package

* Mon Nov 05 2012 Moses Mendoza <moses@puppetlabs.com> - 2.1.4-1
- Update to 2.1.4
- Dynamically define gem_dir macro
- Use ruby_sitearch macro for EPEL, fedora < 17

* Tue Apr 17 2012 Todd Zullinger <tmz@pobox.com> - 2.1.3-2
- Use gem_extdir macro on F-17 and above

* Fri Apr 06 2012 Todd Zullinger <tmz@pobox.com> - 2.1.3-1
- Update to 2.1.3
- Fix license tag

* Sun Apr 01 2012 Todd Zullinger <tmz@pobox.com> - 2.1.2-3
- Revert gem repacking until ruby guidelines are finalized
- Only define gem macros for EPEL, all Fedora releases have them
- Add BuildRoot and clean it manually for EL-5

* Thu Feb 16 2012 Todd Zullinger <tmz@pobox.com> - 2.1.2-2
- Minor cleanups for review
- Changes for building on EL-6 (EL-5s rubygems is too old)

* Mon Jan 16 2012 Michael Stahnke <mastahnke@gmail.com> - 2.1.2-1
- Initial package
