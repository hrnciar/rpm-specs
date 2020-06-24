# Generated from sdoc-0.3.20.gem by gem2rpm -*- rpm-spec -*-
%global gem_name sdoc

Name: rubygem-%{gem_name}
Version: 1.0.0
Release: 5%{?dist}
Summary: RDoc generator to build searchable HTML documentation for Ruby code
# License needs to take RDoc and Darkfish into account apparantly
# https://github.com/voloko/sdoc/issues/27
# SDoc itself is MIT, RDoc part is (GPLv2 or Ruby) and Darkfish is BSD
License: MIT and (GPLv2 or Ruby) and BSD
URL: https://github.com/zzak/sdoc
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Man pages
# https://github.com/voloko/sdoc/pull/49
Source1: sdoc.1
Source2: sdoc-merge.1
# Fix sdoc --version to return the correct version
# https://github.com/zzak/sdoc/issues/125
Patch0: rubygem-sdoc-version-option-fix.patch
# JSON dependency is still required, although upstream dopped the referrence.
# https://github.com/zzak/sdoc/commit/c28efc8d4ebe0a50ed1072f3e4041657b149b634
Requires: rubygem(json)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
SDoc is simply a wrapper for the rdoc command line tool.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%patch0 -p1


%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

# Install man pages into appropriate place.
mkdir -p %{buildroot}%{_mandir}/man1
mv %{SOURCE1} %{buildroot}%{_mandir}/man1
mv %{SOURCE2} %{buildroot}%{_mandir}/man1

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
# Get rid of Bundler
sed -i "/require 'bundler\/setup'/ s/^/#/" ./spec/spec_helper.rb

ruby -Ilib:spec -e 'Dir.glob "./spec/*.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/sdoc
%{_bindir}/sdoc-merge
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{_mandir}/man1/sdoc-merge.1*
%doc %{_mandir}/man1/sdoc.1*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/sdoc.gemspec
%{gem_instdir}/spec

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 26 2018 Vít Ondruch <vondruch@redhat.com> - 1.0.0-1
- Update to SDoc 1.0.0.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Vít Ondruch <vondruch@redhat.com> - 0.4.2-4
- Fix Ruby 2.5 compatibility.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Vít Ondruch <vondruch@redhat.com> - 0.4.2-1
- Update to SDoc 0.4.2.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 05 2015 Josef Stribny <jstribny@redhat.com> - 0.4.1-2
- Add Ruby license to licences

* Mon Aug 18 2014 Josef Stribny <jstribny@redhat.com> - 0.4.1-1
- Update to 0.4.1

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 24 2014 Josef Stribny <jstribny@redhat.com> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Fri Jan 24 2014 Josef Stribny <jstribny@redhat.com> - 0.4.0-2
- Fix disttag

* Thu Jan 23 2014 Josef Stribny <jstribny@redhat.com> - 0.4.0-1
- Update to sdoc 0.4.0
- Run tests
- Fix changelog

* Mon Nov 25 2013 Josef Stribny <jstribny@redhat.com> - 0.4.0-2.rc1
- sdoc 0.4.0 git pre-release to support RDoc 4.0

* Wed Nov 06 2013 Josef Stribny <jstribny@redhat.com> - 0.4.0-1.rc1
- sdoc 0.4.0 git pre-release to support RDoc 4.0

* Tue Aug 06 2013 Josef Stribny <jstribny@redhat.com> - 0.3.20-2
- Add man pages

* Tue Jul 30 2013 Josef Stribny <jstribny@redhat.com> - 0.3.20-1
- Initial package
