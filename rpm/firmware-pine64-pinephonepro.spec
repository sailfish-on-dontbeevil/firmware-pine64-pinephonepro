Name:       firmware-pine64-pinephonepro
Summary:    Firmware blobs for PinePhone Pro
Version:    1.0
Release:    1
Group:      System/Firmware
License:    Redistributable
URL:        https://github.com/sailfish-on-dontbeevil/firmware-pine64-pinephonepro
Source0:     %{name}-%{version}.tar.bz2
Source1:    dptx.bin
Source2:    brcmfmac43455-sdio.bin
Source3:    BCM4345C0.hcd
Source4:    brcmfmac43455-sdio.txt
Source5:    brcmfmac43455-sdio.clm_blob

%description
This package contains firmware for the Pinephone Pro

%prep
ls -lhR .
%setup -q -n %{name}-%{version}

%build
ls -lR .

%install
pwd
ls -lR .
mkdir -p $RPM_BUILD_ROOT/lib/firmware/brcm
mkdir -p $RPM_BUILD_ROOT/lib/firmware/rockchip
cp %{SOURCE1} $RPM_BUILD_ROOT/lib/firmware/rockchip/
cp %{SOURCE2} $RPM_BUILD_ROOT/lib/firmware/brcm/
cp %{SOURCE3} $RPM_BUILD_ROOT/lib/firmware/brcm/
cp %{SOURCE4} $RPM_BUILD_ROOT/lib/firmware/brcm/
cp %{SOURCE5} $RPM_BUILD_ROOT/lib/firmware/brcm/
ln -sf brcmfmac43455-sdio.bin $RPM_BUILD_ROOT/lib/firmware/brcm/brcmfmac43455-sdio.pine64,pinephone-pro.bin
ln -sf BCM4345C0.hcd $RPM_BUILD_ROOT/lib/firmware/brcm/BCM4345C0.pine64,pinephone-pro.hcd
ln -sf brcmfmac43455-sdio.txt $RPM_BUILD_ROOT/lib/firmware/brcm/brcmfmac43455-sdio.pine64,pinephone-pro.txt
ln -sf brcmfmac43455-sdio.clm_blob $RPM_BUILD_ROOT/lib/firmware/brcm/brcmfmac43455-sdio.pine64,pinephone-pro.clm_blob

%files
/lib/firmware/
