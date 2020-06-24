%global gem_name prawn

Summary: A fast and nimble PDF generator for Ruby
Name: rubygem-%{gem_name}
Version: 2.2.2
Release: 4%{?dist}
# afm files are licensed by APAFML, the rest of package is GPLv2 or GPLv3 or Ruby
License: (GPLv2 or GPLv3 or Ruby) and APAFML
URL: http://prawnpdf.org
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem 
# Patch ruby.rb to fix errors due to updated pdf-core dependencies
# https://github.com/prawnpdf/prawn/commit/c504ae4e683017d7afadece084734a9190230cd8
Patch0: prawn-fix-test-errors.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 1.3.6
BuildRequires: rubygem(rspec) >= 3.0
BuildRequires: rubygem(ttfunk) >= 1.5
BuildRequires: rubygem(pdf-reader) >= 1.4.0
BuildRequires: rubygem(pdf-inspector) >= 1.2.1
BuildRequires: rubygem(pdf-core) >= 0.7.0
BuildArch: noarch

%description
Prawn is a pure Ruby PDF generation library that provides a lot of great
functionality while trying to remain simple and reasonably performant.
Here are some of the important features we provide:

- Vector drawing support, including lines, polygons, curves, ellipses, etc.
- Extensive text rendering support, including flowing text and limited inline
  formatting options.
- Support for both PDF builtin fonts as well as embedded TrueType fonts
- A variety of low level tools for basic layout needs, including a simple
  grid system
- PNG and JPG image embedding, with flexible scaling options
- Reporting tools for rendering complex data tables, with pagination support
- Security features including encryption and password protection
- Tools for rendering repeatable content (i.e headers, footers, and page
  numbers)
- Comprehensive internationalization features, including full support for UTF-8
  based fonts, right-to-left text rendering, fallback font support,
  and extension points for customizable text wrapping.
- Support for PDF outlines for document navigation
- Low level PDF features, allowing users to create custom extensions
  by dropping down all the way to the PDF object tree layer.
  (Mostly useful to those with knowledge of the PDF specification)
- Lots of other stuff!

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -n %{gem_name}-%{version}
%gemspec_remove_dep -g pdf-core "~> 0.7.0"
%gemspec_add_dep -g pdf-core ">= 0.7.0"
%patch0

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install -n %{gem_name}-%{version}.gem

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
sed -i "/^require 'bundler'/d" ./spec/spec_helper.rb
sed -i "/^Bundler.setup/d" ./spec/spec_helper.rb

# There are missing font and image files required by test suite.
# These are not bundled in the gem therefore some failures occur.
rspec spec \
  | tee /dev/stderr \
  | grep '850 examples, 103 failures'
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/COPYING
%doc %{gem_instdir}/GPLv2
%doc %{gem_instdir}/GPLv3
%exclude %{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/data/fonts/MustRead.html
%{gem_instdir}/data/fonts/*.afm
%exclude %{gem_instdir}/.yardopts

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%doc %{gem_instdir}/manual

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 08 2018 Christopher Brown <chris.brown@redhat.com> - 2.2.2-1
- Update to 2.2.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 27 2018 Vít Ondruch <vondruch@redhat.com> - 2.1.0-5
- Enable test suite.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Fabio Alessandro Locati <me@fale.io> - 2.1.0-1
- Update to 2.1.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 24 2015 Josef Stribny <jstribny@redhat.com> - 2.0.2-1
- Update to 2.0.2

* Mon Jun 22 2015 Josef Stribny <jstribny@redhat.com> - 2.0.1-1
- Update to 2.0.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Josef Stribny <jstribny@redhat.com> - 1.2.1-1
- Update to 1.2.1

* Mon Jun 23 2014 Josef Stribny <jstribny@redhat.com> - 1.0.0-1
- Update to final 1.0.0 version

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.7.rc2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 06 2014 Josef Stribny <jstribny@redhat.com> - 1.0.0-0.6.rc2
- Relax rubygem-ttfunk dep

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.5.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 17 2013 Josef Stribny <jstribny@redhat.com> - 1.0.0-0.4.rc2
- Fixed license considering .afm

* Thu May 16 2013 Josef Stribny <jstribny@redhat.com> - 1.0.0-0.3.rc2
- *.ttf fonts and rails.png removal

* Tue Apr 16 2013 Josef Stribny <jstribny@redhat.com> - 1.0.0-0.2.rc2
- Move /data to main package

* Mon Apr 15 2013 Josef Stribny <jstribny@redhat.com> - 1.0.0-0.1.rc2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to Prawn 1.0.0.rc2

* Tue Dec 04 2012 Josef Stribny <jstribny@redhat.com> - 0.12.0-1
- Initial package
