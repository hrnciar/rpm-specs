%global octpkg iso2mesh

Name:           octave-%{octpkg}
Version:        1.9.1
Release:        5%{?dist}
Summary:        A 3D surface and volumetric mesh generator for MATLAB/Octave
# Main package: GPLv3+
# Meshfix: GPLv2+
# JMeshLib: GPLv2+
# Tetgen: AGPLv3+
License: GPLv3+ and GPLv2+ and AGPLv3+

URL:            http://iso2mesh.sf.net
# the following utilities are called internally by iso2mesh (stored under a private folder),
# this is needed for making outputs reproducible
Source0:        https://github.com/fangq/iso2mesh/archive/v%{version}/%{octpkg}-%{version}.tar.gz
Source1:        https://github.com/fangq/cork/archive/v0.9/cork-0.9.tar.gz
Source2:        https://github.com/fangq/meshfix/archive/v1.2.1/meshfix-1.2.1.tar.gz
Source3:        http://ftp.mcs.anl.gov/pub/petsc/externalpackages/tetgen1.5.1.tar.gz
Patch0:         meshfix-remove-rpath.patch

ExcludeArch:    armv7hl
BuildRequires:  cmake CGAL-devel SuperLU-devel blas-static gcc-c++ zlib-devel octave-devel

%if 0%{?fedora} >=32
Requires:       octave mpfr-devel boost-devel SuperLU octave-jsonlab octave-jnifti octave-zmat
%else
Requires:       octave CGAL SuperLU octave-jsonlab octave-jnifti octave-zmat
%endif

Requires(post): octave
Requires(postun): octave

%description
Iso2Mesh is a MATLAB/Octave-based mesh generation toolbox,
designed for easy creation of high quality surface and
tetrahedral meshes from 3D volumetric images. It contains
a rich set of mesh processing scripts/programs, working
either independently or interacting with external free
meshing utilities. Iso2Mesh toolbox can directly convert
a 3D image stack, including binary, segmented or gray-scale
images such as MRI or CT scans, into quality volumetric
meshes. This makes it particularly suitable for multi-modality
medical imaging data analysis and multi-physics modeling.
Iso2Mesh is cross-platform and is compatible with both MATLAB
and GNU Octave.

%package -n %{octpkg}-demos
Summary:        Example datasets and scripts for the Iso2Mesh toolbox
BuildArch:      noarch
Requires:       octave octave-%{octpkg}
Recommends:     %{octpkg}-demos

%description -n %{octpkg}-demos
This package contains the demo script and sample datasets for octave-%{octpkg}.

%prep
%setup -q -b 1 -n %{octpkg}-%{version}
%setup -q -T -D -b 2 -n meshfix-1.2.1
%patch0 -p1
%setup -q -T -D -b 3 -n %{octpkg}-%{version}
rm -rf tools/cork
rm -rf tools/meshfix
rm -rf tools/tetgen
mv ../cork-0.9 tools/cork
mv ../meshfix-1.2.1 tools/meshfix
mv ../tetgen1.5.1 tools/tetgen
rm -rf bin/*.mex* bin/*.exe bin/*.dll

cp COPYING.txt COPYING

cat > DESCRIPTION << EOF
Name: %{octpkg}
Version: %{version}
Date: %(date +"%Y-%d-%m")
Title: %{summary}
Author: Qianqian Fang <fangqq@gmail.com>
Maintainer: Qianqian Fang <fangqq@gmail.com>
Description: Iso2Mesh is a MATLAB/Octave-based mesh generation toolbox,
 designed for easy creation of high quality surface and
 tetrahedral meshes from 3D volumetric images. It contains
 a rich set of mesh processing scripts/programs, working
 either independently or interacting with external free
 meshing utilities. Iso2Mesh toolbox can directly convert
 a 3D image stack, including binary, segmented or gray-scale
 images such as MRI or CT scans, into quality volumetric
 meshes. This makes it particularly suitable for multi-modality
 medical imaging data analysis and multi-physics modeling.
 Iso2Mesh is cross-platform and is compatible with both MATLAB
 and GNU Octave.
URL: %{url}
Depends: jnifti, jsonlab, zmat
Categories: Mesh
EOF

cat > INDEX << EOF
iso2mesh >> Iso2Mesh
Iso2Mesh
 advancefront
 barydualmesh
 bbxflatsegment
 binsurface
 bwislands
 cgals2m
 cgalv2m
 deislands2d
 deislands3d
 delendelem
 deletemeshfile
 edgeneighbors
 elemfacecenter
 elemvolume
 extractloops
 extrudecurve
 extrudesurf
 faceneighbors
 fallbackexeext
 fillholes3d
 fillsurf
 finddisconnsurf
 flatsegment
 getexeext
 getintersecttri
 getoptkey
 getplanefrom3pt
 getvarfrom
 highordertet
 i2m
 imedge3d
 img2mesh
 innersurf
 insurface
 internalpoint
 iso2meshver
 isoctavemesh
 jsonopt
 latticegrid
 m2v
 maskdist
 maxsurf
 mcpath
 memmapstream
 mergemesh
 mergestruct
 mergesurf
 mesh2mask
 mesh2vol
 meshabox
 meshacylinder
 meshanellip
 meshasphere
 meshcentroid
 meshcheckrepair
 meshconn
 meshcylinders
 meshedge
 mesheuler
 meshface
 meshgrid5
 meshgrid6
 meshinterp
 meshquality
 meshrefine
 meshremap
 meshreorient
 meshresample
 meshunitsphere
 mwpath
 neighborelem
 nodevolume
 orderloopedge
 orthdisk
 outersurf
 plotedges
 plotmesh
 plotsurf
 plottetra
 qmeshcut
 raysurf
 raytrace
 readasc
 readgts
 readinr
 readmedit
 readmptiff
 readnirfast
 readoff
 readsmf
 readtetgen
 remeshsurf
 removedupelem
 removedupnodes
 removeisolatednode
 removeisolatedsurf
 rotatevec3d
 rotmat2vec
 s2m
 s2v
 saveabaqus
 saveasc
 savebinstl
 savedxf
 savegts
 saveinr
 savejmesh
 savejson
 savemedit
 savemphtxt
 savemsh
 savenirfast
 saveoff
 savesmf
 savestl
 savesurfpoly
 savetetgenele
 savetetgennode
 savevrml
 smoothbinvol
 smoothsurf
 sms
 sortmesh
 surf2mesh
 surf2vol
 surf2volz
 surfaceclean
 surfacenorm
 surfboolean
 surfdiffuse
 surfedge
 surfinterior
 surfpart
 surfplane
 surfreorient
 surfseeds
 surfvolume
 thickenbinvol
 thinbinvol
 uniqedges
 uniqfaces
 v2m
 v2s
 varargin2struct
 vol2mesh
 vol2restrictedtri
 vol2surf
 volface
 volmap2mesh
EOF

mkdir -p inst/

rm -rf base64decode base64encode fast_match_bracket gzipdecode gzipencode \
jdatadecode jdataencode jnifticreate loadjnifti loadjson loadmsgpack \
loadnifti loadubjson lz4decode lz4encode lz4hcdecode lz4hcencode lzipdecode \
lzipencode lzmadecode lzmaencode match_bracket nestbracket2dim nifticreate \
nii2jnii niicodemap niiformat readnifti savebnii savejnifti savejnii \
savemsgpack savenifti saveubjson zlibdecode zlibencode

mv *.m inst/
mv img2mesh.fig inst/

# Fix jmeshlib build flags
sed -e "s|-Wall|%{optflags}|;s|^LIBS = |&$RPM_LD_FLAGS |" \
    -i tools/meshfix/contrib/JMeshLib/test/Makefile

# Fix tetgen build flags
sed -e "s|^\(CXXFLAGS = \).*|\1%{optflags} $RPM_LD_FLAGS|" \
    -e "s|-O0|%{optflags} $RPM_LD_FLAGS|" \
    -i tools/tetgen/makefile

%build
%set_build_flags
pushd tools
# can't use make_build macro below because parallel make with CGAL exhausts
# vm's memory and crash the building process, use sequential make instead
make USERCCFLAGS="%{optflags}"
popd
pushd bin
ln -s tetgen1.5 tetgen
popd

mkdir inst/bin
pushd bin
for exec in *; do
   ln -s %{_libexecdir}/%{octpkg}/$exec ../inst/bin/$exec
done
popd
%octave_pkg_build

%if 0%{?fedora} <=30
   %global octave_tar_suffix any-none
%endif

%install
%octave_pkg_install
install -m 0755 -vd  %{buildroot}%{_libexecdir}/%{octpkg}
install -m 0755 -vp  bin/* %{buildroot}%{_libexecdir}/%{octpkg}/

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%license COPYING.txt
%doc README.txt
%doc Content.txt
%doc AUTHORS.txt
%doc ChangeLog.txt
%dir %{octpkgdir}
%dir %{octpkgdir}/doc
%dir %{octpkgdir}/bin
%{_libexecdir}/%{octpkg}
%{octpkgdir}/doc/*
%{octpkgdir}/bin/*
%{octpkgdir}/*.m
%{octpkgdir}/*.fig
%doc %{octpkgdir}/doc-cache
%{octpkgdir}/packinfo

%files -n %{octpkg}-demos
%license COPYING.txt
%doc sample

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Jerry James <loganjerry@gmail.com> - 1.9.1-4
- Rebuild for mpfr 4
- Use Fedora build flags when building jmeshlib and tetgen

* Fri Oct 11 2019 Qianqian Fang <fangqq@gmail.com> - 1.9.1-3
- Define octave package-level dependency via the DESCRIPTION file
- Remove gmp-devel from Requires

* Thu Oct 10 2019 Qianqian Fang <fangqq@gmail.com> - 1.9.1-2
- Fix licenses
- Move binaries to libexec

* Wed Oct 02 2019 Qianqian Fang <fangqq@gmail.com> - 1.9.1-1
- Initial package
