# Generated from rbvmomi-1.2.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rbvmomi

Name: rubygem-%{gem_name}
Version: 1.11.2
Release: 7%{?dist}
Summary: Ruby interface to the VMware vSphere API
License: MIT
URL: https://github.com/vmware/rbvmomi
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/vmware/rbvmomi.git && cd rbvmomi
# git checkout v1.11.2 && tar czvf rbvmomi-1.11.2-tests.tgz test/
Source1: %{gem_name}-%{version}-tests.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.8.7
BuildRequires: rubygem(nokogiri)
BuildRequires: rubygem(builder)
BuildRequires: rubygem(test-unit)
BuildArch: noarch

%description
Ruby interface to the VMware vSphere API.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}


%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x

# Fix rpmlint issues.
for f in \
  analyze-vim-declarations \
  benchmark \
  collisions \
  merge-internal-vmodl \
  merge-manual-vmodl \
  ;
do
  sed -i '/#!.*env ruby/d' %{buildroot}%{gem_instdir}/devel/$f.rb
done

%check
pushd .%{gem_instdir}
tar xzvf %{SOURCE1}

# We don't really care about code coverage.
sed -i "/[sS]imple[cC]ov/ s/^/#/" test/test_helper.rb

ruby -Ilib:test -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/rbvmomish
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/LICENSE
%{gem_instdir}/exe
%{gem_libdir}
%exclude %{gem_instdir}/rbvmomi.gemspec
%{gem_instdir}/vmodl.db
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CONTRIBUTORS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/devel
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/examples

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Vít Ondruch <vondruch@redhat.com> - 1.11.2-1
- Update to rbvmomi 1.11.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jul 17 2014 Vít Ondruch <vondruch@redhat.com> - 1.8.1-1
- Update to rbvmomi 1.8.1.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 14 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.3-8
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 01 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1.2.3-5
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 21 2011 Michal Fojtik <mfojtik@redhat.com> - 1.2.3-3
- Added vmodl.db back, since it's required dependency

* Mon Jul 11 2011 Francesco Vollero <fvollero@redhat.com> - 1.2.3-2
- Fix License to MIT
- Removed the >= 0 versions from rubygems Requires
- Add Requires and BuildRequires: ruby(abi) = 1.8
- Executed the test suite.

* Tue Jun 14 2011 Francesco Vollero <fvollero@redhat.com> - 1.2.3-1
- Initial package
