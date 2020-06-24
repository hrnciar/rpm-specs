# Generated from chunky_png-1.2.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name chunky_png

Summary: Pure ruby library for read/write, chunk-level access to PNG files
Name: rubygem-%{gem_name}
Version: 1.3.11
Release: 3%{?dist}
License: MIT
URL: http://wiki.github.com/wvanbergen/chunky_png
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: fix-failing-spec-with-dimension-hash.patch
BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
This pure Ruby library can read and write PNG images without depending on
an external image library, like RMagick. It tries to be memory efficient and
reasonably fast.
It supports reading and writing all PNG variants that are defined in the
specification, with one limitation: only 8-bit color depth is supported. It
supports all transparency, interlacing and filtering options the PNG
specifications allows. It can also read and write textual metadata from PNG
files. Low-level read/write access to PNG chunks is also possible.
This library supports simple drawing on the image canvas and simple operations
like alpha composition and cropping. Finally, it can import from and export to
RMagick for interoperability.


%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

pushd .%{gem_instdir}
%patch0 -p1
popd

%build


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
find %{buildroot} -iname .gitignore -exec rm -f {} \;
find %{buildroot} -iname .yardopts -exec rm -f {} \;
rm -f %{buildroot}%{gem_instdir}/.infinity_test

%check
pushd .%{gem_instdir}
# Don't use Bundler.
sed -i "/require 'bundler\/setup'/ s/^/#/" spec/spec_helper.rb

rspec spec
popd


%files
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_instdir}/.*
%doc %{gem_instdir}/spec
%doc %{gem_instdir}/tasks
%doc %{gem_instdir}/*.rdoc
%doc %{gem_instdir}/%{gem_name}.gemspec
%doc %{gem_instdir}/benchmarks
%doc %{gem_instdir}/Rakefile
%doc %{gem_instdir}/README.md
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/Gemfile
%doc %{gem_docdir}
%exclude %{gem_cache}
%{gem_spec}


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Christopher Brown <chris.brown@redhat.com> - 1.3.11-1
- Update to chunky_png 1.3.11

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Mar 13 2013 Vít Ondruch <vondruch@redhat.com> - 1.2.7-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Update to chunky_png 1.2.7.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 02 2012 Vít Ondruch <vondruch@redhat.com> - 1.2.0-4
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Chris Lalancette <clalance@redhat.com> - 1.2.0-2
- Updates from package review

* Fri Jul 08 2011 Chris Lalancette <clalance@redhat.com> - 1.2.0-1
- Initial package
