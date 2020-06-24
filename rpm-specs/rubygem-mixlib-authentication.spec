# Generated from mixlib-authentication-1.1.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mixlib-authentication

# EPEL6 lacks rubygems-devel package that provides these macros
%if %{?el6}0
%global gem_dir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%global gem_instdir %{gem_dir}/gems/%{gem_name}-%{version}
%global gem_docdir %{gem_dir}/doc/%{gem_name}-%{version}
%global gem_libdir %{gem_instdir}/lib
%global gem_cache %{gem_dir}/cache/%{gem_name}-%{version}.gem
%global gem_spec %{gem_dir}/specifications/%{gem_name}-%{version}.gemspec
%endif

%if %{?el6}0 || %{?fc16}0
%global rubyabi 1.8
%else
%global rubyabi 1.9.1
%endif

Summary: Simple per-request authentication
Name: rubygem-%{gem_name}
Version: 1.4.2
Release: 6%{?dist}
License: ASL 2.0
URL: http://github.com/chef/mixlib-authentication
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(rubygems)
Requires: rubygem(mixlib-log)
%if 0%{?fedora} >= 19
Requires: ruby(release)
BuildRequires: ruby(release)
%else
Requires: ruby(abi) = %{rubyabi}
BuildRequires: ruby(abi) = %{rubyabi}
%endif
BuildRequires: ruby
BuildRequires: ruby(rubygems)
# Needed to run checks:
%{!?el6:BuildRequires: rubygem(rspec)}
%{!?el6:BuildRequires: rubygems-devel}
%{!?el6:BuildRequires: rubygem(mixlib-log)}
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Mixlib::Authentication provides a class-based header signing authentication
object.

%package doc
Summary: Documentation for %{name}

Requires: %{name} = %{version}-%{release}

%description doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T

%if 0%{?fedora} >= 19
%gem_install -n %{SOURCE0}
%else
mkdir -p .%{gem_dir}
gem install -V \
  --local \
  --install-dir $(pwd)/%{gem_dir} \
  --force --rdoc \
  %{SOURCE0}
%endif

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
%if %{?el6}0
# spec on EL6 is too old; need RSpec2 
%else
pushd .%{gem_instdir}
rspec -Ilib spec/mixlib/authentication/
popd
%endif

%files
%doc %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/%{gem_name}.gemspec

%files doc
%doc %{gem_instdir}/NOTICE
%{gem_instdir}/Rakefile
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/spec
%doc %{gem_docdir}

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Julian C. Dunn <jdunn@aquezada.com> - 1.4.2-1
- Update to 1.4.2 (bz#1424339)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 08 2013 Josef Stribny <jstribny@redhat.com> - 1.3.0-4
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 23 2012 Julian C. Dunn <jdunn@aquezada.com> - 1.3.0-1
- Upgrade to 1.3.0
- Drop rubygem-mixlib-authentication-1.1.4-spec.patch

* Sun Apr 29 2012 Jonas Courteau <rpms@courteau.org> - 1.1.4-1
- Repackaged for fc17
- New upstream version
- Patch to fix broken spec (fixed in upstream commit fe5cd0116)

* Fri Mar 19 2010 Matthew Kent <matt@bravenet.com> - 1.1.2-2
- Let check phase fail.
- Fix duplicate inclusion of Rakefile.

* Wed Mar 17 2010 Matthew Kent <matt@bravenet.com> - 1.1.2-1
- Initial package
