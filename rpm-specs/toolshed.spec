Name:           toolshed
Version:        20180731hg6906ea14f8f5
Release:        5%{?dist}
Summary:        Cross-development toolkit for use with the Tandy Color Computer

License:        Public Domain
URL:            http://sourceforge.net/projects/toolshed/
Source0:        %{name}-%{version}-noroms.tar.gz
# toolshed contains disassmbled code that we cannot ship.  Therefore we use
# this script to remove the disassmbled code before shipping it.
# Generate the Mercurial snapshot from the SourceForge repository:
# hg archive -t tgz toolshed-<date>hg<hash>.tar.gz
# Now invoke this script while in the tarball's directory:
# ./generate-tarball.sh <date>hg<hash>
Source1: generate-tarball.sh

BuildRequires:  gcc
BuildRequires:  fuse-devel
BuildRequires:  discount


%description
ToolShed is a package of utilities to perform cross-development from
Windows, Linux or Mac OS X computers to the Tandy Color Computer and
Dragon microcomputers. Tools are included to read/write both OS-9 RBF
disk images and CoCo Disk BASIC disk images, create WAV and CAS files
and much more.


%prep
%setup -q

# Turn-off weird doc permissions...
chmod 0644 doc/*


%build
make %{?_smp_mflags} CFLAGS="%{optflags} -I../../../include -DSYSV" \
        -C build/unix


%install
mkdir -p %{buildroot}%{_bindir}
make %{?_smp_mflags} -C build/unix install INSTALLDIR=%{buildroot}%{_bindir} DOCDIR=%{buildroot}%{_docdir}/%{name}


%files
%{_bindir}/*
%{_docdir}/%{name}/ToolShed.html


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20180731hg6906ea14f8f5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20180731hg6906ea14f8f5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180731hg6906ea14f8f5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20180731hg6906ea14f8f5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 02 2018 John W. Linville <linville@tuxdriver.com> 20180731hg6906ea14f8f5-2
- Add BuildRequires for discount to handle markdown sources

* Tue Jul 31 2018 John W. Linville <linville@tuxdriver.com> 20180731hg6906ea14f8f5-1
- Update from current upstream

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20150416hg6f0dcb7087fe-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20150416hg6f0dcb7087fe-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150416hg6f0dcb7087fe-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150416hg6f0dcb7087fe-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20150416hg6f0dcb7087fe-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20150416hg6f0dcb7087fe-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20150416hg6f0dcb7087fe-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 16 2015 John W. Linville <linville@tuxdriver.com> 20150416hg6f0dcb7087fe-1
- Initial import
