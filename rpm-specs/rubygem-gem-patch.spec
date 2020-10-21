# Generated from gem-patch-0.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gem-patch

Summary: RubyGems plugin for patching gems
Name: rubygem-%{gem_name}
Version: 0.1.6
Release: 11%{?dist}
License: MIT
URL: http://github.com/strzibny/gem-patch
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:  rubygems-devel 
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(bundler)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
gem-patch is a RubyGems plugin that helps to patch gems
without manually opening and rebuilding them.
It opens a given .gem file, extracts it, patches it with
system `patch` command, clones its spec, updates the file list
and builds the patched gem.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

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

%check
pushd .%{gem_instdir}
# Avoid requiring minitest 4
ruby -rrubygems -Ilib - << \EOF
  module Kernel
    alias :orig_gem :gem
    remove_method :gem

    def gem gem_name, *requirements
      if gem_name == 'minitest'
        orig_gem 'minitest'
      else
        orig_gem gem_name, *requirements
      end
    end
  end
  Dir.glob('./test/**/test_*.rb').each { |t| require t }
EOF

%files
%dir %{gem_instdir}
%{gem_libdir}

%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENCE

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/test

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 09 2019 Pavel Valena <pvalena@redhat.com> - 0.1.6-7
- Fix FTBFS: add bundler to BuildRequires

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jun 22 2015 Josef Stribny <jstribny@redhat.com> - 0.1.6-1
- Update to 0.1.6

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 10 2014 Josef Stribny <jstribny@redhat.com> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 07 2014 Josef Stribny <jstribny@redhat.com> - 0.1.5-1
- Update to gem-patch 0.1.5

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Josef Stribny <jstribny@redhat.com> - 0.1.4-1
- Update to gem-patch 0.1.4

* Wed Feb 27 2013 Josef Stribny <jstribny@redhat.com> - 0.1.3-3
- F-19: Rebuild for ruby 2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 22 2012 Josef Strzibny <jstribny@redhat.com> - 0.1.3-1
- Upgraded to version 0.1.3
- Moved tests to -doc subpackage
- Moved rakefile.rb to -doc subpackage
- Moved LICENCE from -doc subpackage
- Adjusted description of the package

* Thu Oct 18 2012 Josef Strzibny <jstribny@redhat.com> - 0.1.2-1
- Initial package
