%global	gem_name	rmagick

%define setIMver() \
%if 0%{?fedora}%{?rhel} == %1 \
BuildRequires:	ImageMagick-devel = %2\
Requires:		ImageMagick%{?_isa} = %2\
%endif \
%{nil}

Name:		rubygem-%{gem_name}
Version:	4.1.2
Release:	5%{?dist}

Summary:	Ruby binding to ImageMagick
License:	MIT
URL:		https://github.com/rmagick/rmagick
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# %%{SOURCE2} %%{version}
Source1:	rubygem-%{gem_name}-%{version}-full.tar.gz

BuildRequires:	gcc
BuildRequires:	rubygems-devel 
BuildRequires:	ruby-devel
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(minitest4)
BuildRequires:	rubygem(rspec)
BuildRequires:	rubygem(pry)
# Due to test/RMagick/rmmain.c test_Magick_version(), for now
# we specify the exact version for ImageMagick
%if 0%{?fedora}
%setIMver 34 1:6.9.11.27
%setIMver 33 1:6.9.11.27
%setIMver 32 1:6.9.11.27
%endif

Obsoletes:	ruby-RMagick < 2.13.2
Provides:	ruby-RMagick = %{version}-%{release}
Provides:	ruby-RMagick%{?_isa} = %{version}-%{release}
Provides:	ruby(RMagick) = %{version}-%{release}

%description
RMagick is an interface between Ruby and ImageMagick.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

Obsoletes:	ruby-RMagick-doc < 2.13.2
Provides:	ruby-RMagick-doc = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
%setup -q -T -n %{gem_name}-%{version} -b 1
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# permission
find . -name \*.rb -or -name \*.gif | xargs chmod ugo-x 

%build
export CFLAGS="%{optflags}"
# Make sure that .so is to be created newly
rm -rf ./%{gem_extdir_mri}
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
cp -a \
	doc \
	examples \
	%{buildroot}%{gem_instdir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} \
	%{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}%{gem_instdir}
rm -rf \
	.editorconfig \
	.github \
	.gitignore .[^.]*.yml \
	wercker.yml \
	.rspec \
	.simplecov \
	.yardopts \
	Doxyfile Gemfile Rakefile \
	before_*.sh \
	doc/.cvsignore \
	*.gemspec \
	test/ \
	spec/ \
	ext/ \
	benchmarks/ \
	.circleci/ \
	.ruby-version \
	%{nil}
popd

%check
export RUBYLIB=$(pwd):$(pwd)/lib:$(pwd)/test:%{buildroot}%{gem_extdir_mri}
export COVERAGE=false

rspec spec/

%files
%dir	%{gem_instdir}/
%license	%{gem_instdir}/LICENSE
%doc	%{gem_instdir}/CONTRIBUTING.md
%doc	%{gem_instdir}/CHANGELOG.md
%doc	%{gem_instdir}/README.md

%{gem_libdir}/
%{gem_instdir}/deprecated/
%{gem_extdir_mri}/
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}/
%doc	%{gem_instdir}/CODE_OF_CONDUCT.md
%doc	%{gem_instdir}/doc/
%doc	%{gem_instdir}/examples/

%changelog
* Tue Aug 11 2020 Michael Cronenworth <mike@cchtml.com> - 4.1.2-5
- Rebuild for ImageMagick 6.9.11-27

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 25 2020 Michael Cronenworth <mike@cchtml.com> - 4.1.2-3
- Rebuild for ImageMagick 6.9.11-22

* Wed Jun 03 2020 Michael Cronenworth <mike@cchtml.com> - 4.1.2-2
- Rebuild for ImageMagick 6.9.11-16

* Mon Apr 20 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.1.2-1
- 4.1.2

* Fri Feb 14 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 4.0.0-1
- 4.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.0-3
- F-32: rebuild against ruby27

* Mon Jan 13 2020 Michael Cronenworth <mike@cchtml.com> - 3.2.0-2
- Rebuild for ImageMagick 6.9.10-86

* Tue Dec 31 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Tue Dec 31 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.16.0-28
- Once clean up spec file, especially remove conditions for branches
  which are no longer supported

* Tue Nov 26 2019 Michael Cronenworth <mike@cchtml.com> - 2.16.0-27
- Rebuild for ImageMagick 6.9.10-75

* Fri Oct 04 2019 Pete Walter <pwalter@fedoraproject.org> - 2.16.0-26
- Rebuild for ImageMagick 6.9.10-67

* Sat Sep 21 2019 Pete Walter <pwalter@fedoraproject.org> - 2.16.0-25
- Rebuild for ImageMagick 6.9.10-65

* Fri Sep 13 2019 Michael Cronenworth <mike@cchtml.com> - 2.16.0-24
- Rebuild for ImageMagick 6.9.10-64

* Fri Aug 16 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.16.0-23
- Add BR properly for rawhide

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Pete Walter <pwalter@fedoraproject.org> - 2.16.0-21
- Rebuild for ImageMagick 6.9.10-28

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.16.0-19
- F-30: rebuild against ruby26

* Fri Jan 11 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.16.0-18
- Fix failed test for 6.9.10.23 for now

* Wed Jan 2 2019 Michael Cronenworth <mike@cchtml.com> - 2.16.0-18
- Rebuild for ImageMagick 6.9.10-23

* Mon Sep 3 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.16.0-17
- Remove failed test for 6.9.10 for now

* Tue Aug 28 2018 Michael Cronenworth <mike@cchtml.com> - 2.16.0-17
- Rebuild for ImageMagick 6.9.10

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.16.0-15
- Rescue failing tests by 6.9.9-38 internal change

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.16.0-13
- Rebuilt for switch to libxcrypt

* Thu Jan 04 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.16.0-12
- F-28: rebuild for ruby25

* Sat Dec 23 2017 Michael Cronenworth <mike@cchtml.com> - 2.16.0-11
- Rebuild for ImageMagick 6.9.9-27

* Wed Nov 22 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.16.0-10
- Rescue failing tests by 6.9.9-22 internal change

* Thu Nov 09 2017 Michael Cronenworth <mike@cchtml.com> - 2.16.0-9
- Rebuild for ImageMagick 6.9.9-22

* Wed Oct 11 2017 Michael Cronenworth <mike@cchtml.com> - 2.16.0-8
- Rebuild for ImageMagick 6.9.9-19

* Fri Sep 29 2017 Michael Cronenworth <mike@cchtml.com> - 2.16.0-7
- Rebuild for ImageMagick 6.9.9-15

* Fri Sep 15 2017 Michael Cronenworth <mike@cchtml.com> - 2.16.0-6
- Rebuild for ImageMagick 6.9.9-13

* Wed Sep 06 2017 Michael Cronenworth <mike@cchtml.com> - 2.16.0-5
- Rebuild for ImageMagick 6

* Thu Aug  3 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.16.0-4.1
- rebuild against new ImageMagick

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 11 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.16.0-2
- F-26: rebuild for ruby24

* Wed Aug 17 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.16.0-1
- 2.16.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.4-2
- F-24: rebuild againt ruby23

* Mon Jan 11 2016 Mamoru TASAKA <mtasaka@fedoraproject.org>
- F-24: rebuild against new ImageMagick

* Thu Dec 10 2015 Mamoru TASAKA <mtasaka@fedoraproject.org>
- F-22+: rebuild against new ImageMagick

* Mon Aug 17 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.4-1
- 2.15.4

* Wed Jul 22 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.3-1
- 2.15.3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun  3 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.2-1
- 2.15.2

* Mon Jun  1 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.1-1
- 2.15.1

* Fri May 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org>
- F-23: rebuild against new ImageMagick

* Wed Apr 29 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.15.0-1
- 2.15.0

* Tue Apr 28 2015 Mamoru TASAKA <mtasaka@fedoraproject.org>
- F-23: rebuild against new ImageMagick

* Wed Apr  1 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.14.0-1
- 2.14.0

* Thu Mar 12 2015 Mamoru TASAKA <mtasaka@fedoraproject.org>
- F-23: rebuild against new ImageMagick

* Fri Jan 30 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13.4-2
- Add some comments for patches
- Fix permission

* Wed Jan 28 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.13.4-1
- Initial package
