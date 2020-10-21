%global gem_name ncursesw

Name:           rubygem-%{gem_name}
Version:        1.4.10
Release:        2%{?dist}
Summary:        Ruby wrapper for the ncurses library, with wide character support
License:        LGPLv2+
URL:            http://github.com/sup-heliotrope/ncursesw-ruby
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# This is a C extension linked against MRI, it's not compatible with other 
# interpreters. So we require MRI specifically instead of ruby(release).
Requires:       ruby
BuildRequires:  ruby
BuildRequires:  rubygems-devel
BuildRequires:  ruby-devel
BuildRequires:  ncurses-devel
BuildRequires:  gcc
# rubygem Requires/Provides are automatically generated in F21+
%if ! (0%{?fedora} >= 21 || 0%{?rhel} >= 8)
Requires:       ruby(rubygems)
Provides:       rubygem(%{gem_name}) = %{version}
%endif

%description
This wrapper provides access to the functions, macros, global variables and 
constants of the ncurses library. These are mapped to a Ruby module named 
"Ncurses". Functions and external variables are implemented as singleton 
functions of the module Ncurses.

The ncursesw gem is a fork with improved wide character support.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
# examples are under a wide variety of licenses
License:        LGPLv2+ and MIT and MIT with advertising and LDPL

%description doc
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/specifications/ .%{gem_dir}/doc/ %{buildroot}%{gem_dir}
mkdir -p %{buildroot}%{gem_instdir}
cp -pa .%{gem_instdir}/{lib,examples} %{buildroot}%{gem_instdir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/extconf.rb/

%files
%license COPYING
%doc README.md Changes THANKS TODO
%dir %{gem_instdir}
%{gem_extdir_mri}
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/examples

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Dan Callaghan <djc@djc.id.au> - 1.4.10-1
- upstream release 1.4.10
- build steps updated to match current Ruby packaging conventions

* Mon Apr 13 2015 Dan Callaghan <dcallagh@redhat.com> - 1.4.9-1
- upstream release 1.4.9

* Mon Jan 27 2014 Dan Callaghan <dcallagh@redhat.com> - 1.4.3-1
- Initial package
